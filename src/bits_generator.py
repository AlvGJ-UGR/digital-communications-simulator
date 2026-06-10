"""
bits_generator.py
-----------------
Random bit sequence generator with optional seeding for reproducibility.
"""

import numpy as np


def generate_bits(N: int, seed: int = None) -> np.ndarray:
    """
    Generate a random binary sequence of length N.

    Parameters
    ----------
    N    : int  – Number of bits to generate.
    seed : int  – Optional RNG seed for reproducible results.

    Returns
    -------
    np.ndarray of dtype int, shape (N,), values in {0, 1}.
    """
    rng = np.random.default_rng(seed)
    return rng.integers(0, 2, size=N, dtype=int)


def bits_to_str(bits: np.ndarray) -> str:
    """Return bits array as a compact binary string, e.g. '0110100...'."""
    return "".join(bits.astype(str))


def str_to_bits(s: str) -> np.ndarray:
    """Parse a binary string back to a numpy int array."""
    return np.array(list(s), dtype=int)
