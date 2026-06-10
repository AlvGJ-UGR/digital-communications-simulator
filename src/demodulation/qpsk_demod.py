"""
demodulation/qpsk_demod.py
--------------------------
QPSK maximum-likelihood (hard-decision) detector.

Gray-code decision regions (matching qpsk_mod mapping):
    Re{r} ≥ 0, Im{r} ≥ 0  →  00
    Re{r} <  0, Im{r} ≥ 0  →  01
    Re{r} <  0, Im{r} <  0  →  11
    Re{r} ≥ 0, Im{r} <  0  →  10
"""

import numpy as np


def qpsk_demod(rx: np.ndarray) -> np.ndarray:
    """
    Hard-decision QPSK detector. Returns a flat bit array.

    Parameters
    ----------
    rx : np.ndarray, shape (N,), dtype complex – Received symbols.

    Returns
    -------
    bits : np.ndarray, shape (2N,), dtype int
    """
    i_bits = (np.real(rx) < 0).astype(int)   # MSB
    q_bits = (np.imag(rx) < 0).astype(int)   # LSB
    return np.column_stack([i_bits, q_bits]).flatten()
