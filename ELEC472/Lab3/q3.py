import matplotlib.pyplot as plt
import lab3 as l3
import numpy as np
import scipy.signal as sci

window_size = 401
cutoff = 5
sampling_freq = 500 # same as previous questions

#lowpass filter: 
filter_coefficients_low = sci.firwin(window_size, cutoff, window='hamming', pass_zero=True, 
scale=True, fs=sampling_freq) 

# plot the created filter: 

freq, pow1 = l3.psd(filter_coefficients_low, sampling_freq)

plt.figure()
plt.plot(freq, pow1)
plt.title('Low-pass Filter')
plt.grid()
plt.show()

#highpass filter: 
filter_coefficients_high = sci.firwin(window_size, cutoff, window='hamming', pass_zero=False, 
scale=True, fs=sampling_freq) 

# plot the created filter: 

freq, pow1 = l3.psd(filter_coefficients_high, sampling_freq)

plt.figure()
plt.plot(freq, pow1)
plt.title('High-pass Filter')
plt.grid()
plt.show()

# import x and convolve with filter: use high pass to cut offset (spike at beginning)

ecg_timeseries_full=[]

with open('ecg.csv') as f:
    for line in f.readlines():
        ecg_timeseries_full.append(float(line.strip()))

x = ecg_timeseries_full[71740:81060]

x_filtered = np.convolve(x, filter_coefficients_high)

# print filtered ECG signal

freq, pow1 = l3.psd(x_filtered, sampling_freq)

plt.figure()
plt.plot(freq, pow1)
plt.title('Filtered ECG Signal')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.grid()
plt.show()

# welch algorithm on x_filtered 

# WELCH METHOD

freq, pxx_welch = l3.pwelch(x_filtered, fs=sampling_freq, window='hamming',)

plt.figure()
plt.plot(freq,pxx_welch)
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


# part 12 - butterworth IIR 

filter_order = 7
Wn = 5

b, a = sci.butter(filter_order, Wn, btype='high', analog=False, output='ba', fs=sampling_freq) 

filtered_signal = sci.lfilter(b, a, x)

# Plot original and filtered signal
plt.figure(figsize=(8, 4))
t = np.linspace(0, 1, len(x), endpoint=False)
plt.plot(t, x, label="Original Signal", alpha=0.5)
plt.plot(t, filtered_signal, label="Filtered Signal", linewidth=2)
plt.legend()
plt.title("Butterworth Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
# Plot original and filtered signal
plt.figure(figsize=(8, 4))
t = np.linspace(0, 1, len(x), endpoint=False)
plt.plot(t, x, label="Original Signal", alpha=0.5)
plt.plot(t, filtered_signal, label="Filtered Signal", linewidth=2)
plt.ylim([-2, 2])
plt.legend()
plt.title("Butterworth Filter")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()