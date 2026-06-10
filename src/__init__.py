"""
digital-communications-simulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Top-level package exposing the full simulation API.
"""

from .bits_generator            import generate_bits
from .modulation                import bpsk_mod, qpsk_mod, qam_mod
from .channel                   import awgn, rayleigh_channel
from .demodulation              import bpsk_demod, qpsk_demod, qam_demod
from .metrics                   import ber, ber_bpsk_theory, ber_qpsk_theory, ber_qam_theory
from .utils                     import (
    snr_to_eb_n0, eb_n0_to_snr, spectral_efficiency_table,
    plot_constellation, plot_constellation_comparison,
)

__all__ = [
    "generate_bits",
    "bpsk_mod", "qpsk_mod", "qam_mod",
    "awgn", "rayleigh_channel",
    "bpsk_demod", "qpsk_demod", "qam_demod",
    "ber", "ber_bpsk_theory", "ber_qpsk_theory", "ber_qam_theory",
    "snr_to_eb_n0", "eb_n0_to_snr", "spectral_efficiency_table",
    "plot_constellation", "plot_constellation_comparison",
]
