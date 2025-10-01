"""
KB_luen_observer(d).py
For ELEC 446: question 1.c) of assignment 2. 
Simulates noise on range signal of observer from part (c).
Tested at r_sigma = 1 and 0.01; noise is too small to see at the smaller value, but its there!
Observations: the estimated path is centered on true path, but 
    varies slightly in radius and in angle. Noisy signals cause
    error in robot's true location. 
    Additionally, noise is more pronounced on theta for the same
    reasons as outlined in (c); since the angle is based on two 
    sets of noisy signals (last position and current), therefore
    introducing lag + doubling the range of possible noise. 
Author: Kay Burnham <19kob1@queensu.ca>

Modified from example code fws_beacons_observer.py
Example Author: Joshua A. Marshall <joshua.marshall@queensu.ca>
GitHub: https://github.com/botprof/agv-examples
"""

# %%
# SIMULATION SETUP

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mobotpy.integration import rk_four
from mobotpy.models import DiffDrive

# Set the simulation time [s] and the sample period [s]
SIM_TIME = 20
T = 0.1

# Create an array of time values [s]
t = np.arange(0.0, SIM_TIME, T)
N = np.size(t)

# %%
# VEHICLE SETUP

# Set the wheelbase of the vehicle [m]
ELL = 0.25

# Std dev for range measurement noise [m]
r_sigma = 0.01

# DIFFDRIVE vehicle initialization 
vehicle = DiffDrive(ELL)

# %%
# CREATE A MAP OF BEACONS

# Set the size [m] of a square map
D_MAP = 20.0

# Set number of beacons -- preserves modularity 
N_BEACONS = 2

# Place beacons on map at (4,3) and (3, -7)
f_map = np.zeros((2, N_BEACONS))
f_map[:, 0] = (4, 3)
f_map[:, 1] = (3, -7)

# %%
# FUNCTION TO MODEL RANGE TO BEACONS


def range_sensor(x, f_map):
    """
    Function to model the range sensor.

    Parameters
    ----------
    x : ndarray
        An array of length 2 representing the robot's position.
    f_map : ndarray
        An array of size (2, N_BEACONS) containing map beacon locations.

    Returns
    -------
    ndarray
        The range to each beacon in the map.
    """

    # Compute the range to each beacon from the current robot position
    r = np.zeros(N_BEACONS)
    # r_noisy = np.zeros(N_BEACONS)
    for j in range(0, N_BEACONS):
        r[j] = np.sqrt((f_map[0, j] - x[0]) ** 2 + (f_map[1, j] - x[1]) ** 2)

    # Return the array of measurements
    return r


# %%
# FUNCTION TO IMPLEMENT THE OBSERVER


def diff_observer(q, u, r, f_map):
    """
    Function to implement an observer for the robot's pose.

    Parameters
    ----------
    q : ndarray
        An array of length 3 representing the (last) robot's pose.
    u : ndarray
        An array of length 2 representing the robot's inputs.
    r : ndarray
        An array of length N_BEACONS representing the range to each beacon.
    f_map : ndarray
        An array of size (2, N_BEACONS) containing map beacon locations.

    Returns
    -------
    ndarray
        The estimated pose of the robot.
    """

    # Compute the Jacobian matrices (i.e., linearize about current estimate)
    F = np.zeros((3, 3))
    F = np.eye(3) + T * np.array(
        [
            [
                1,
                0,
                - 0.5 * np.cos(q[2]),
            ],
            [
                0,
                1,
                - 0.5 * np.sin(q[2]),
            ],
            [0, 0, 1],
        ]
    )
    H = np.zeros((N_BEACONS, 3))
    for j in range(0, N_BEACONS):
        H[j, :] = np.array(
            [
                -(f_map[0, j] - q[0]) / range_sensor(q, f_map)[j],
                -(f_map[1, j] - q[1]) / range_sensor(q, f_map)[j],
                0,
            ]
        )

    # Check the observability of this system
    observability_matrix = H
    for j in range(1, 3):
        observability_matrix = np.concatenate(
            (observability_matrix, H @ np.linalg.matrix_power(F, j)), axis=0
        )
    if np.linalg.matrix_rank(observability_matrix) < 3:
        raise ValueError("System is not observable!")

    # Set the desired poles at lambda_z (change these as desired)
    lambda_z = np.array([0.7, 0.8, 0.9])
    # Compute the observer gain
    L = signal.place_poles(F.T, H.T, lambda_z).gain_matrix.T
    # Use the pseudo-inverse to compute the observer gain (when overdetermined)
    # L = signal.place_poles(F.T, np.eye(4), lambda_z).gain_matrix @ np.linalg.pinv(H)

    # Predict the state using the inputs and the robot's kinematic model
    # q_new = [[a*T for a in vehicle.f(q, u)]]
    q_new = q + T * vehicle.f(q, u)

    # Correct the state using the range measurements
    q_new = q_new + L @ (r - range_sensor(q, f_map))

    # Return the estimated state
    return q_new


# %%
# RUN SIMULATION

# Initialize arrays that will be populated with our inputs and states
x = np.zeros((3, N))
u = np.zeros((2, N))
x_hat = np.zeros((3, N))

# Set path for vehicle [m, m/s]
r_path = 5.0
bot_speed = 0.25
angular_speed = (2 * np.pi) * bot_speed / r_path 

# Set the initial pose [m, m, rad], velocities [m/s, rad/s]
x[0, 0] = -3.0
x[1, 0] = 2.0
x[2, 0] = np.pi / 6.0
u[0, 0] = (r_path - ELL / 2) * angular_speed
u[1, 0] = (r_path + ELL / 2) * angular_speed

# Just drive around and try to localize!
for k in range(1, N):
    # Measure the actual range to each beacon
    r = range_sensor(x[:, k - 1], f_map)
    # Simulate noise (centered on 0-mean)
    r_noisy = r + r_sigma * (np.random.rand(1) - 0.5)
    # Use the range measurements to estimate the robot's state
    x_hat[:, k] = diff_observer(x_hat[:, k - 1], u[:, k - 1], r_noisy, f_map)
    # Choose some new inputs
    u[0, k] = (r_path - ELL / 2) * angular_speed
    u[1, k] = (r_path + ELL / 2) * angular_speed
    # Simulate the robot's motion
    x[:, k] = rk_four(vehicle.f, x[:, k - 1], u[:, k - 1], T)

# %%
# MAKE SOME PLOTS


# Function to wrap angles to [-pi, pi]
def wrap_to_pi(angle):
    """Wrap angles to the range [-pi, pi]."""
    return (angle + np.pi) % (2 * np.pi) - np.pi


# Change some plot settings (optional)
plt.rc("text", usetex=True)
plt.rc("text.latex", preamble=r"\usepackage{cmbright,amsmath,bm}")
plt.rc("savefig", format="pdf")
plt.rc("savefig", bbox="tight")

# Plot the position of the vehicle in the plane
fig1 = plt.figure(1)
plt.plot(f_map[0, :], f_map[1, :], "C4*", label="Beacon")
plt.plot(x[0, :], x[1, :], "C0", label="Actual")
plt.plot(x_hat[0, :], x_hat[1, :], "C1--", label="Estimated")
plt.axis("equal")
X_L, Y_L, X_R, Y_R, X_B, Y_B, X_C, Y_C = vehicle.draw(x[0, 0], x[1, 0], x[2, 0])
plt.fill(X_L, Y_L, "k")
plt.fill(X_R, Y_R, "k")
plt.fill(X_C, Y_C, "k")
plt.fill(X_B, Y_B, "C2", alpha=0.5, label="Start")
X_L, Y_L, X_R, Y_R, X_B, Y_B, X_C, Y_C = vehicle.draw(
    x[0, N - 1], x[1, N - 1], x[2, N - 1]
)
plt.fill(X_L, Y_L, "k")
plt.fill(X_R, Y_R, "k")
plt.fill(X_C, Y_C, "k")
plt.fill(X_B, Y_B, "C3", alpha=0.5, label="End")
plt.xlabel(r"$x$ [m]")
plt.ylabel(r"$y$ [m]")
plt.legend()

# Plot the states as a function of time
fig2 = plt.figure(2)
fig2.set_figheight(6.4)
ax2a = plt.subplot(411)
plt.plot(t, x[0, :], "C0", label="Actual")
plt.plot(t, x_hat[0, :], "C1--", label="Estimated")
plt.grid(color="0.95")
plt.ylabel(r"$x$ [m]")
plt.setp(ax2a, xticklabels=[])
plt.legend()
ax2b = plt.subplot(412)
plt.plot(t, x[1, :], "C0", label="Actual")
plt.plot(t, x_hat[1, :], "C1--", label="Estimated")
plt.grid(color="0.95")
plt.ylabel(r"$y$ [m]")
plt.setp(ax2b, xticklabels=[])
ax2c = plt.subplot(413)
plt.plot(t, wrap_to_pi(x[2, :]) * 180.0 / np.pi, "C0", label="Actual")
plt.plot(t, wrap_to_pi(x_hat[2, :]) * 180.0 / np.pi, "C1--", label="Estimated")
plt.ylabel(r"$\theta$ [deg]")
plt.grid(color="0.95")
plt.setp(ax2c, xticklabels=[])
plt.xlabel(r"$t$ [s]")


# Show all the plots to the screen
plt.show()
