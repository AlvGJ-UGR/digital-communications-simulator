"""
modulation/qam.py
-----------------
Square M-QAM modulator (M = 4, 16, 64, 256, …).

- Independent I/Q axes with Gray coding per axis.
- Normalised so that average symbol energy = 1.
"""

import numpy as np


def _gray_code(n: int) -> int:
    """Convert integer n to its Gray-code equivalent."""
    return n ^ (n >> 1)


def _build_qam_map(M: int) -> dict:
    """
    Build a dict: bit-tuple → complex symbol (unit energy).

    Parameters
    ----------
    M : int – Constellation order, must be a perfect square power-of-2.
    """
    k = int(np.log2(M))
    if 2 ** k != M or int(np.sqrt(M)) ** 2 != M:
        raise ValueError(f"M={M} is not a perfect-square power of 2.")

    sqM = int(np.sqrt(M))
    k_half = k // 2  # bits per axis

    # Create axis levels: odd integers symmetrically around 0
    levels = np.arange(-(sqM - 1), sqM, 2, dtype=float)  # [-3,-1,1,3] for 16-QAM

    # Gray-code ordering of levels
    gray_order = [_gray_code(i) for i in range(sqM)]
    gray_levels = np.empty(sqM)
    for idx, g in enumerate(gray_order):
        gray_levels[g] = levels[idx]

    mapping = {}
    for i in range(sqM):
        for q in range(sqM):
            i_bits = tuple(int(b) for b in format(i, f"0{k_half}b"))
            q_bits = tuple(int(b) for b in format(q, f"0{k_half}b"))
            symbol = gray_levels[i] + 1j * gray_levels[q]
            mapping[i_bits + q_bits] = symbol

    # Normalise to unit average energy
    avg_energy = np.mean(np.abs(list(mapping.values())) ** 2)
    norm = np.sqrt(avg_energy)
    return {k: v / norm for k, v in mapping.items()}


# Cache maps to avoid rebuilding on every call
_MAP_CACHE: dict[int, dict] = {}


def qam_mod(bits: np.ndarray, M: int = 16) -> np.ndarray:
    """
    Map a bit stream to M-QAM symbols with unit average energy.

    Parameters
    ----------
    bits : np.ndarray, shape (N,) – must be divisible by log2(M).
    M    : int – Constellation order (default 16).

    Returns
    -------
    symbols : np.ndarray, shape (N / log2(M),), dtype complex128
    """
    k = int(np.log2(M))
    if bits.size % k != 0:
        raise ValueError(f"{M}-QAM requires bits divisible by {k}.")

    if M not in _MAP_CACHE:
        _MAP_CACHE[M] = _build_qam_map(M)
    mapping = _MAP_CACHE[M]

    groups = bits.reshape(-1, k)
    symbols = np.array([mapping[tuple(b)] for b in groups], dtype=complex)
    return symbols
