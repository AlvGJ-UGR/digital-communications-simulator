"""
channel/rayleigh.py
-------------------
Flat-fading Rayleigh channel followed by AWGN.

In a Rayleigh fading channel every symbol is multiplied by an independent
complex Gaussian coefficient h ~ CN(0,1), modelling rich multipath with
no line-of-sight component:

    r[n] = h[n] · s[n] + w[n]

The receiver is assumed to have perfect channel state information (CSI) and
applies a single-tap zero-forcing equaliser:

    ŝ[n] = r[n] / h[n]

This is intentionally the simplest possible flat-fading model and is useful
for illustrating the BER floor that arises compared to the AWGN case.
"""

import numpy as np
from .awgn import awgn


def rayleigh_channel(signal: np.ndarray, snr_db: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Pass `signal` through a flat Rayleigh fading channel with AWGN.

    Parameters
    ----------
    signal : np.ndarray – Transmitted complex symbols.
    snr_db : float      – Per-symbol SNR in dB (before fading).

    Returns
    -------
    rx_eq  : np.ndarray – Equalised received signal (same shape as input).
    h      : np.ndarray – Realised fading coefficients.
    """
    if not np.iscomplexobj(signal):
        signal = signal.astype(complex)

    # Complex Gaussian fading coefficients
    h = (np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape)) / np.sqrt(2)

    # Faded signal → AWGN
    faded = h * signal
    rx = awgn(faded, snr_db)

    # Zero-forcing equalisation (perfect CSI)
    rx_eq = rx / h

    return rx_eq, h
