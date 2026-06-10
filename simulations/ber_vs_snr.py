"""
simulations/ber_vs_snr.py
--------------------------
BER vs Eb/N0 sweep for BPSK, QPSK, 16-QAM and 64-QAM.

Produces:
    results/plots/ber_vs_snr.png

Usage:
    python -m simulations.ber_vs_snr
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from src.bits_generator         import generate_bits
from src.modulation             import bpsk_mod, qpsk_mod, qam_mod
from src.channel                import awgn
from src.demodulation           import bpsk_demod, qpsk_demod, qam_demod
from src.metrics.ber            import ber, ber_bpsk_theory, ber_qpsk_theory, ber_qam_theory

# ── simulation parameters ───────────────────────────────────────────────────
N_BITS    = 200_000          # bits per SNR point
SNR_RANGE = np.arange(-4, 22, 1)   # Eb/N0 in dB
BER_FLOOR = 1e-6             # stop plotting below this

# ── colour palette ──────────────────────────────────────────────────────────
_GRID   = "#0D0D1A"
_TEXT   = "#E0E0E0"
COLORS  = {
    "BPSK":   "#00B4D8",
    "QPSK":   "#7B61FF",
    "16-QAM": "#F72585",
    "64-QAM": "#FFB703",
}


def simulate_ber(modname: str, snr_range: np.ndarray, n_bits: int) -> np.ndarray:
    """Run Monte-Carlo BER simulation for one modulation scheme."""
    ber_sim = []

    for snr_db in snr_range:
        bits = generate_bits(n_bits)

        if modname == "BPSK":
            tx  = bpsk_mod(bits)
            rx  = awgn(tx.astype(complex), snr_db)
            hat = bpsk_demod(rx)
            b   = ber(bits, hat)

        elif modname == "QPSK":
            n   = (n_bits // 2) * 2
            tx  = qpsk_mod(bits[:n])
            rx  = awgn(tx, snr_db)
            hat = qpsk_demod(rx)
            b   = ber(bits[:n], hat)

        elif modname == "16-QAM":
            n   = (n_bits // 4) * 4
            tx  = qam_mod(bits[:n], M=16)
            rx  = awgn(tx, snr_db)
            hat = qam_demod(rx, M=16)
            b   = ber(bits[:n], hat)

        elif modname == "64-QAM":
            n   = (n_bits // 6) * 6
            tx  = qam_mod(bits[:n], M=64)
            rx  = awgn(tx, snr_db)
            hat = qam_demod(rx, M=64)
            b   = ber(bits[:n], hat)

        else:
            raise ValueError(f"Unknown modulation: {modname}")

        ber_sim.append(max(b, 1e-7))   # avoid log(0)

    return np.array(ber_sim)


def run(save: bool = True) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(9, 6), facecolor=_GRID)
    ax.set_facecolor(_GRID)

    eb_theory = np.linspace(SNR_RANGE[0], SNR_RANGE[-1], 300)

    schemes = {
        "BPSK":   (ber_bpsk_theory(eb_theory), ber_bpsk_theory),
        "QPSK":   (ber_qpsk_theory(eb_theory), ber_qpsk_theory),
        "16-QAM": (ber_qam_theory(eb_theory, M=16), lambda x: ber_qam_theory(x, M=16)),
        "64-QAM": (ber_qam_theory(eb_theory, M=64), lambda x: ber_qam_theory(x, M=64)),
    }

    for name, (theory_ber, _) in schemes.items():
        color = COLORS[name]

        # Theoretical curve
        ax.semilogy(eb_theory, theory_ber, "-", color=color, linewidth=1.8,
                    alpha=0.55, label=f"{name} – theory")

        # Monte-Carlo simulation
        print(f"  Simulating {name} …", flush=True)
        sim_ber = simulate_ber(name, SNR_RANGE, N_BITS)
        ax.semilogy(SNR_RANGE, sim_ber, "o", color=color, markersize=5,
                    markeredgewidth=0.5, markeredgecolor="white",
                    label=f"{name} – simulation")

    # ── formatting ──────────────────────────────────────────────────────────
    ax.set_xlabel("$E_b/N_0$ (dB)", color=_TEXT, fontsize=12)
    ax.set_ylabel("Bit Error Rate (BER)", color=_TEXT, fontsize=12)
    ax.set_title("BER vs $E_b/N_0$  –  AWGN Channel", color=_TEXT, fontsize=14, pad=12)

    ax.set_xlim(SNR_RANGE[0], SNR_RANGE[-1])
    ax.set_ylim(BER_FLOOR, 1.0)
    ax.grid(True, which="both", color="#2A2A3E", linewidth=0.6)
    ax.tick_params(colors=_TEXT, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor("#444455")

    leg = ax.legend(fontsize=8.5, facecolor="#1A1A2E", labelcolor=_TEXT,
                    framealpha=0.85, ncol=2, loc="upper right")

    plt.tight_layout()

    if save:
        out = os.path.join(os.path.dirname(__file__), "..", "results", "plots", "ber_vs_snr.png")
        fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=_GRID)
        print(f"  Saved → {os.path.abspath(out)}")

    return fig


if __name__ == "__main__":
    print("Running BER vs SNR simulation …")
    run()
    print("Done.")
