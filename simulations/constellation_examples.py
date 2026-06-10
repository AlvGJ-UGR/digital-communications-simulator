"""
simulations/constellation_examples.py
---------------------------------------
Generate constellation diagrams (clean and noisy) for BPSK, QPSK, 16-QAM.

Produces:
    results/plots/constellation_clean_noisy.png
    results/plots/constellation_snr_sweep.png

Usage:
    python -m simulations.constellation_examples
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from src.bits_generator  import generate_bits
from src.modulation      import bpsk_mod, qpsk_mod, qam_mod
from src.channel         import awgn

_GRID  = "#0D0D1A"
_TEXT  = "#E0E0E0"
_CLEAN = "#00B4D8"
_NOISY = "#7B61FF"
_BDR   = "#F72585"


def _scatter(ax, tx, rx, title, max_pts=3000):
    ax.set_facecolor(_GRID)
    ax.axhline(0, color=_BDR, lw=0.6, alpha=0.45)
    ax.axvline(0, color=_BDR, lw=0.6, alpha=0.45)

    n = min(len(rx), max_pts)
    idx = np.random.choice(len(rx), n, replace=False)
    ax.scatter(rx[idx].real, rx[idx].imag, s=3, alpha=0.3, color=_NOISY, label="Rx")

    unique = np.unique(tx)
    ax.scatter(unique.real, unique.imag, s=70, zorder=5, color=_CLEAN,
               edgecolors="white", lw=0.5, label="Ideal")

    ax.set_title(title, color=_TEXT, fontsize=10, pad=6)
    ax.tick_params(colors=_TEXT, labelsize=7)
    for sp in ax.spines.values():
        sp.set_edgecolor("#333344")
    ax.legend(fontsize=7, facecolor="#1A1A2E", labelcolor=_TEXT, framealpha=0.7)


def _make_symbols(N=20_000):
    """Return dict of tx symbols for BPSK, QPSK, 16-QAM."""
    bits = generate_bits(N * 4)          # enough bits for all
    return {
        "BPSK":   bpsk_mod(bits[:N]).astype(complex),
        "QPSK":   qpsk_mod(bits[: (N // 2) * 2]),
        "16-QAM": qam_mod(bits[: (N // 4) * 4], M=16),
    }


def plot_clean_noisy(snr_db: float = 10.0, save: bool = True) -> plt.Figure:
    """Side-by-side clean vs noisy for each scheme at a given SNR."""
    tx_all = _make_symbols()
    schemes = list(tx_all.keys())

    fig = plt.figure(figsize=(15, 5), facecolor=_GRID)
    gs  = gridspec.GridSpec(1, 3, figure=fig, wspace=0.28)

    for col, name in enumerate(schemes):
        tx = tx_all[name]
        rx = awgn(tx, snr_db)
        ax = fig.add_subplot(gs[col])
        _scatter(ax, tx, rx, f"{name}  –  {snr_db:.0f} dB SNR")

    fig.suptitle("Constellation Diagrams: Clean vs Noisy", color=_TEXT,
                 fontsize=14, y=1.02)
    plt.tight_layout()

    if save:
        out = os.path.join(os.path.dirname(__file__), "..", "results", "plots",
                           "constellation_clean_noisy.png")
        fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=_GRID)
        print(f"  Saved → {os.path.abspath(out)}")

    return fig


def plot_snr_sweep(scheme: str = "16-QAM", save: bool = True) -> plt.Figure:
    """
    Show how the constellation of a single scheme degrades across SNR levels.
    """
    snr_levels = [0, 5, 10, 20]
    N = 10_000

    bits = generate_bits(N * 4)
    if scheme == "BPSK":
        tx = bpsk_mod(bits[:N]).astype(complex)
    elif scheme == "QPSK":
        tx = qpsk_mod(bits[: (N // 2) * 2])
    else:
        tx = qam_mod(bits[: (N // 4) * 4], M=16)

    fig = plt.figure(figsize=(20, 5), facecolor=_GRID)
    gs  = gridspec.GridSpec(1, 4, figure=fig, wspace=0.28)

    for col, snr in enumerate(snr_levels):
        rx = awgn(tx, snr)
        ax = fig.add_subplot(gs[col])
        _scatter(ax, tx, rx, f"{scheme}  –  SNR = {snr} dB")

    fig.suptitle(f"{scheme} Constellation at Various SNR Levels",
                 color=_TEXT, fontsize=14, y=1.02)
    plt.tight_layout()

    if save:
        out = os.path.join(os.path.dirname(__file__), "..", "results", "plots",
                           "constellation_snr_sweep.png")
        fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=_GRID)
        print(f"  Saved → {os.path.abspath(out)}")

    return fig


if __name__ == "__main__":
    print("Generating constellation diagrams …")
    plot_clean_noisy(snr_db=10)
    plot_snr_sweep("16-QAM")
    print("Done.")
