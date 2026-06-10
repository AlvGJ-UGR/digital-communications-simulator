"""
modulation/qpsk.py
------------------
Quadrature Phase-Shift Keying (QPSK) modulator – Gray coded.

Mapping (Gray code):
    bits 00 → +1+1j  (phase  45°)
    bits 01 → -1+1j  (phase 135°)
    bits 11 → -1-1j  (phase 225°)
    bits 10 → +1-1j  (phase 315°)

Normalised so that average symbol energy = 1.
"""

import numpy as np

# Gray-coded QPSK constellation
_QPSK_MAP = {
    (0, 0):  1 + 1j,
    (0, 1): -1 + 1j,
    (1, 1): -1 - 1j,
    (1, 0):  1 - 1j,
}
_NORM = np.sqrt(2)


def qpsk_mod(bits: np.ndarray) -> np.ndarray:
    """
    Map a bit stream to complex QPSK symbols (unit average energy).

    Parameters
    ----------
    bits : np.ndarray, shape (N,) – must be divisible by 2.

    Returns
    -------
    symbols : np.ndarray, shape (N/2,), dtype complex128
    """
    if bits.size % 2 != 0:
        raise ValueError("QPSK requires an even number of bits.")
    pairs = bits.reshape(-1, 2)
    symbols = np.array([_QPSK_MAP[tuple(b)] for b in pairs], dtype=complex)
    return symbols / _NORM
