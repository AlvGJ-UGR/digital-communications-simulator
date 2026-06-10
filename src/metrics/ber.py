"""
metrics/ber.py
--------------
Bit Error Rate (BER) computation – simulated and theoretical.
"""

import numpy as np
from scipy.special import erfc


# ---------------------------------------------------------------------------
# Empirical BER
# ---------------------------------------------------------------------------

def ber(tx_bits: np.ndarray, rx_bits: np.ndarray) -> float:
    """
    Compute the empirical Bit Error Rate.

    Parameters
    ----------
    tx_bits : np.ndarray – Transmitted bits.
    rx_bits : np.ndarray – Received (decoded) bits.

    Returns
    -------
    float – Fraction of bits received in error.
    """
    if tx_bits.size != rx_bits.size:
        raise ValueError("tx_bits and rx_bits must have the same length.")
    return float(np.mean(tx_bits != rx_bits))


# ---------------------------------------------------------------------------
# Theoretical BER curves
# ---------------------------------------------------------------------------

def _q_function(x: np.ndarray) -> np.ndarray:
    """Q(x) = 0.5 * erfc(x / sqrt(2))."""
    return 0.5 * erfc(x / np.sqrt(2))


def ber_bpsk_theory(eb_n0_db: np.ndarray) -> np.ndarray:
    """
    Theoretical BER for BPSK over AWGN:
        BER = Q( sqrt(2 * Eb/N0) )

    Parameters
    ----------
    eb_n0_db : array-like – Eb/N0 in dB.

    Returns
    -------
    np.ndarray – BER values.
    """
    eb_n0 = 10.0 ** (np.asarray(eb_n0_db) / 10.0)
    return _q_function(np.sqrt(2.0 * eb_n0))


def ber_qpsk_theory(eb_n0_db: np.ndarray) -> np.ndarray:
    """
    Theoretical BER for QPSK over AWGN.

    QPSK has the same BER as BPSK when expressed as a function of Eb/N0:
        BER = Q( sqrt(2 * Eb/N0) )

    Parameters
    ----------
    eb_n0_db : array-like – Eb/N0 in dB.
    """
    return ber_bpsk_theory(eb_n0_db)


def ber_qam_theory(eb_n0_db: np.ndarray, M: int = 16) -> np.ndarray:
    """
    Approximate theoretical BER for square M-QAM over AWGN (Gray coding):
        BER ≈ (4/log2(M)) * (1 - 1/sqrt(M)) * Q( sqrt(3*log2(M)*Eb/N0 / (M-1)) )

    Parameters
    ----------
    eb_n0_db : array-like – Eb/N0 in dB.
    M        : int         – Constellation order.
    """
    k = np.log2(M)
    eb_n0 = 10.0 ** (np.asarray(eb_n0_db) / 10.0)
    arg = np.sqrt(3.0 * k * eb_n0 / (M - 1))
    coeff = (4.0 / k) * (1.0 - 1.0 / np.sqrt(M))
    return coeff * _q_function(arg)
