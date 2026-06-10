"""
demodulation/qam_demod.py
-------------------------
M-QAM minimum-distance (hard-decision) detector.

For each received symbol the nearest constellation point is found via
exhaustive search over the pre-built symbol table (fast for M ≤ 256).
"""

import numpy as np
from src.modulation.qam import _build_qam_map, _MAP_CACHE


def qam_demod(rx: np.ndarray, M: int = 16) -> np.ndarray:
    """
    Hard-decision M-QAM detector.

    Parameters
    ----------
    rx : np.ndarray, shape (N,), dtype complex – Received symbols.
    M  : int – Constellation order (must match the modulator).

    Returns
    -------
    bits : np.ndarray, shape (N * log2(M),), dtype int
    """
    if M not in _MAP_CACHE:
        _MAP_CACHE[M] = _build_qam_map(M)
    mapping = _MAP_CACHE[M]

    bit_labels = list(mapping.keys())          # list of bit-tuples
    constellation = np.array(list(mapping.values()))  # complex array

    k = int(np.log2(M))
    bits_out = np.empty(rx.size * k, dtype=int)

    for idx, r in enumerate(rx):
        distances = np.abs(constellation - r) ** 2
        nearest = int(np.argmin(distances))
        bits_out[idx * k : (idx + 1) * k] = bit_labels[nearest]

    return bits_out
