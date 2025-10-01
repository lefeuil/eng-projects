
import numpy as np
import matplotlib.pyplot as plt
import random

class Ant:
    """Ant colony matrix
    """
    def __init__(self):
        self.tour = []
        self.cost = 0

def tour_length(tour, L):
    tour.append(tour[0])  # Close the loop
    return sum(L[tour[i], tour[i+1]] for i in range(len(tour) - 1))

def roulette_wheel_selection(P):
    r = np.random.rand()  # Generate a random number between 0 and 1
    C = np.cumsum(P)  # Compute the cumulative sum of probabilities
    j = np.where(r <= C)[0][0]  # Find the index of the first element where r <= C
    return j


def ant_colony_optimization(x, y, q, max_iter, num_ants, alpha, beta, rho):
    """Ant Colony Optimization (ACO) setup

    Args:
        x (list): x coordinates
        y (list): y coordinates
        q (int): q constant
        max_iter (int): Maximum number of iteration
        num_ants (int): Number of ants
        alpha (float): Phromone coefficient
        beta (float): Preference for shortest path
        rho (float): Evaporation rate

    Returns:
        final_tour, best_cost
    """

    n=len(x)
    assert len(x)==len(y)

    # Initialize the distance matrix
    L = np.zeros((n, n))
    # Fill the distance matrix
    for i in range(n - 1):
        for j in range(i + 1, n):
            L[i, j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            L[j, i] = L[i, j]

    tau0 = 10 * q / (n * np.mean(L))  # Initial phromone

    # Initialize parameters
    eta = 1 / L  # Desirability
    tau = tau0 * np.ones((n, n))  # Pheromone matrix
    best_cost = np.zeros(max_iter)  # Best cost values
    best_sol = {'cost': np.inf}  # Best solution holder

    # Create ants
    ants = [Ant() for _ in range(num_ants)]

    # Perform the search operation
    for it in range(max_iter):  # Stop when maximum iteration reached
        for k in range(num_ants):  # Iterate over all the ants
            # Starting at a random location
            ants[k].tour = [random.randint(0, n-1)]
            
            for l in range(1, n):  # Iterate over all the locations
                i = ants[k].tour[-1]
                ##### Implement your solution here  
                # write the formula to calculate probability 
                # START OF YOUR CODE

                P = (tau[i,:] ** alpha) * (eta[i,:] ** beta)

                # END OF YOUR CODE

                # Sets the probability of visiting already-visited nodes to 0
                P[ants[k].tour] = 0
                # Normalize probabilities
                P = P / np.sum(P)
                
                # Roulette Wheel Selection method to select the next location
                j = roulette_wheel_selection(P)
                ants[k].tour.append(j)
            
            # Updating the cost function for kth ant
            ants[k].cost = tour_length(ants[k].tour, L)
            
            if ants[k].cost < best_sol['cost']:
                best_sol = {'tour': ants[k].tour, 'cost': ants[k].cost}  # Update best solution

        # Update Phromones
        for k in range(num_ants):
            tour = ants[k].tour + [ants[k].tour[0]]  # Append the start to the end to complete the tour
            
            for l in range(n):
                i = tour[l]
                j = tour[l+1]

                ##### Implement your solution here  
                # write the formula to update phromones
                # START OF YOUR CODE
                
                tau[i,j] = (1-rho) * tau[i,j] + q / L[i,j]

                # END OF YOUR CODE
        
        # Update best cost
        best_cost[it] = best_sol['cost']
        
        # Printing cost updates
        print(f"Iteration {it+1}: Best Cost = {best_cost[it]}")

    # Results
    final_tour = best_sol['tour'] + [best_sol['tour'][0]]
    print(f"Best path: {final_tour}")

    return final_tour, best_cost



if __name__=='__main__':

    # Our goal is to find the optimal path amongst few locations, while 
    # visiting each node only once. we will use ant colony optimization
    # algorithm to solve this.

    # Setup the problem
    n = 16  # Total number of locations
    x = np.array([36, 13, 76, 99, 27, 62, 94, 74, 31, 67, 56, 39, 66, 44, 20, 55])
    y = np.array([59, 76, 38, 89, 66, 83, 5, 50, 42, 61, 80, 10, 87, 67, 64, 32])

    # Visualize the locations
    plt.figure(1)
    plt.scatter(x, y, 100, color='yellow', edgecolor='black', linewidth=1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)

    # Parameters
    max_iter = 1000  # Maximum number of iterations
    num_ants = 100  # Number of ants
    q = 10  # q constant
    alpha = 0.9  # Pheromone coefficient
    beta = 1  # Preference for shortest path
    rho = 0.1  # Evaporation rate

    final_tour, best_cost = ant_colony_optimization(x, y, q, max_iter, num_ants, alpha, beta, rho)

    # Visualizing the travel path
    plt.figure()
    # use scatter plot when max_iter is 1
    plt.plot(x[final_tour], y[final_tour], 'k-o', markersize=10, markerfacecolor='yellow', linewidth=1.5)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


    # Visualize the cost curve
    plt.figure()
    plt.plot(best_cost, linewidth=2)
    plt.xlabel('Iteration')
    plt.ylabel('Best Cost')
    plt.grid(True)
    plt.show()



