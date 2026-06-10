"""
modulation/bpsk.py
------------------
Binary Phase-Shift Keying (BPSK) modulator.

Mapping:
    bit 0 → symbol -1  (phase π)
    bit 1 → symbol +1  (phase 0)
"""

import numpy as np


def bpsk_mod(bits: np.ndarray) -> np.ndarray:
    """
    Map bits to real BPSK symbols in {-1, +1}.

    Parameters
    ----------
    bits : np.ndarray, shape (N,), values in {0, 1}

    Returns
    -------
    symbols : np.ndarray, shape (N,), dtype float64
    """
    if bits.ndim != 1:
        raise ValueError("bpsk_mod expects a 1-D bit array.")
    return (2 * bits - 1).astype(float)
