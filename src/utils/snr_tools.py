"""
utils/snr_tools.py
------------------
Helpers for SNR / Eb·N0 conversions and spectral-efficiency tables.
"""

import numpy as np


def snr_to_eb_n0(snr_db: float, bits_per_symbol: int) -> float:
    """
    Convert symbol SNR (Es/N0) in dB to bit SNR (Eb/N0) in dB.

        Eb/N0 [dB] = Es/N0 [dB] − 10·log10(bits_per_symbol)

    Parameters
    ----------
    snr_db          : float – Es/N0 in dB.
    bits_per_symbol : int   – log2(M).
    """
    return snr_db - 10.0 * np.log10(bits_per_symbol)


def eb_n0_to_snr(eb_n0_db: float, bits_per_symbol: int) -> float:
    """Inverse of snr_to_eb_n0."""
    return eb_n0_db + 10.0 * np.log10(bits_per_symbol)


def spectral_efficiency_table() -> list[dict]:
    """
    Return a list of dicts with scheme properties for display.

    Each dict has keys: name, M, bits_per_symbol, robustness.
    """
    return [
        {"name": "BPSK",    "M": 2,   "bits_per_symbol": 1, "robustness": "Very High"},
        {"name": "QPSK",    "M": 4,   "bits_per_symbol": 2, "robustness": "High"},
        {"name": "8-PSK",   "M": 8,   "bits_per_symbol": 3, "robustness": "Medium"},
        {"name": "16-QAM",  "M": 16,  "bits_per_symbol": 4, "robustness": "Medium-Low"},
        {"name": "64-QAM",  "M": 64,  "bits_per_symbol": 6, "robustness": "Low"},
        {"name": "256-QAM", "M": 256, "bits_per_symbol": 8, "robustness": "Very Low"},
    ]
