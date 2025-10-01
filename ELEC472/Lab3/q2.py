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
x = ecg_timeseries_full[71740:81060]

# PERIODOGRAM

freq1, pow1 = l3.psd(x, sampling_freq)
# Remember, x is the same data created earlier, covering samples 71,740 to 81,060
plt.figure()
plt.plot(freq1,pow1)
plt.ylim([0, 0.005])
plt.title('Periodogram')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()
plt.show()

plt.figure()
plt.plot(freq1,10*np.log10(pow1))
plt.title('Periodogram Log scale')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()
plt.show()

# WELCH METHOD

freq, pxx_welch = l3.pwelch(x, fs=sampling_freq, window='hamming',)

plt.figure()
plt.plot(freq,pxx_welch)
plt.ylim([0, .007])
plt.title('Periodogram')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()
plt.show()

plt.figure()
plt.plot(freq,10*np.log10(pxx_welch))
plt.title('Periodogram Log scale')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()
plt.show()