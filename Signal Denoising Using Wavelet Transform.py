import numpy as np
import pywt
import matplotlib.pyplot as plt

# Generate a noisy signal
np.random.seed(42)
time = np.linspace(0, 1, num=1000)
signal = np.sin(2 * np.pi * 10 * time)  # Sine wave with frequency 10 Hz
noise = np.random.normal(0, 0.5, time.shape)  # Gaussian noise
noisy_signal = signal + noise

# Perform wavelet transform
wavelet = 'db4'  # Daubechies wavelet
coeffs = pywt.wavedec(noisy_signal, wavelet, level=4)

# Threshold the coefficients to remove noise
threshold = 0.3
coeffs_denoised = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]

# Reconstruct the denoised signal
denoised_signal = pywt.waverec(coeffs_denoised, wavelet)

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, noisy_signal, label="Noisy Signal", color='gray')
plt.plot(time, signal, label="Original Signal", color='blue', linestyle='--', alpha=0.7)
plt.legend()
plt.title("Noisy Signal vs Original Signal")

plt.subplot(2, 1, 2)
plt.plot(time, denoised_signal, label="Denoised Signal", color='green')
plt.plot(time, signal, label="Original Signal", color='blue', linestyle='--', alpha=0.7)
plt.legend()
plt.title("Denoised Signal vs Original Signal")

plt.tight_layout()
plt.show()
