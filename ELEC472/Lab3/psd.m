function [freq1, pow1] = psd(input_signal, Fs)
 
% calculating the DFT using the FFT algorithm
dft1 = fft(input_signal); 
 
% getting rid of the second half of the DFT (just a duplicate of the first half)
dft1 = dft1(1:floor(length(input_signal)/2)+1); 
 
pow1 = (1/(Fs*length(input_signal))) * abs(dft1(1:end)).^2;
freq1 = 0:Fs/length(input_signal):Fs/2;
