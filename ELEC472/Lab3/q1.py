import matplotlib.pyplot as plt
import lab3 as l3
import numpy as np

ecg_timeseries_full=[]

with open('ecg.csv') as f:
    for line in f.readlines():
        ecg_timeseries_full.append(float(line.strip()))

# from the hardware specs used for recording this data, we know that 
# the sampling frequency is 500Hz
sampling_freq = 500

plt.figure()
plt.title('Entire ECG signal')
plt.plot(ecg_timeseries_full)
plt.show()

# the time-series is too long, so we're going to take a small segment
x = ecg_timeseries_full[71740:81060]

plt.figure()
plt.plot(range(len(x)), x)
plt.title('Cropped ECG signal')
plt.show()


