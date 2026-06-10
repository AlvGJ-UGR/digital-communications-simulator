"""
demodulation/bpsk_demod.py
--------------------------
BPSK maximum-likelihood (hard-decision) detector.

Decision rule:
    Re{r} ≥ 0  →  bit 1
    Re{r} <  0  →  bit 0
"""

import numpy as np


def bpsk_demod(rx: np.ndarray) -> np.ndarray:
    """
    Hard-decision BPSK detector.

    Parameters
    ----------
    rx : np.ndarray – Received samples (real or complex; only Re part used).

    Returns
    -------
    bits : np.ndarray, shape (N,), dtype int, values in {0, 1}
    """
    return (np.real(rx) >= 0).astype(int)
