"""
channel/awgn.py
---------------
Additive White Gaussian Noise (AWGN) channel.

The channel model is:
    r(t) = s(t) + n(t)

where n(t) is zero-mean complex (or real) Gaussian noise with variance
σ² = P_signal / SNR_linear.

For complex signals, noise is split equally between I and Q components so
that the total noise power equals the target.
"""

import numpy as np


def awgn(signal: np.ndarray, snr_db: float) -> np.ndarray:
    """
    Add AWGN to a signal at the specified SNR.

    The noise power is computed relative to the **measured** signal power,
    so the function is agnostic to modulation scheme or normalisation.

    Parameters
    ----------
    signal : np.ndarray – Transmitted symbols (real or complex).
    snr_db : float      – Signal-to-Noise Ratio in dB.

    Returns
    -------
    rx : np.ndarray – Received signal with same shape and dtype as `signal`.
    """
    snr_linear = 10.0 ** (snr_db / 10.0)
    sig_power = np.mean(np.abs(signal) ** 2)
    noise_power = sig_power / snr_linear

    if np.iscomplexobj(signal):
        # Equal power in I and Q
        noise = np.sqrt(noise_power / 2) * (
            np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape)
        )
    else:
        noise = np.sqrt(noise_power) * np.random.randn(*signal.shape)

    return signal + noise
