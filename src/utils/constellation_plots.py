"""
utils/constellation_plots.py
-----------------------------
Reusable Matplotlib helpers for constellation diagrams.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# ── colour palette (matches the project's visual identity) ──────────────────
_CLEAN   = "#00B4D8"   # cyan-blue  – ideal symbols
_NOISY   = "#7B61FF"   # violet     – received symbols
_GRID    = "#1E1E2E"   # near-black – background
_ACCENT  = "#F72585"   # magenta    – decision boundaries
_TEXT    = "#E0E0E0"


def plot_constellation(
    tx_symbols: np.ndarray,
    rx_symbols: np.ndarray | None = None,
    title: str = "Constellation Diagram",
    ax: plt.Axes | None = None,
    max_points: int = 2000,
) -> plt.Axes:
    """
    Plot a constellation diagram.

    Parameters
    ----------
    tx_symbols : ideal (pre-noise) complex symbols.
    rx_symbols : noisy received symbols (optional).
    title      : subplot title.
    ax         : existing Axes to draw on (creates figure if None).
    max_points : cap on number of noisy points plotted (readability).
    """
    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(5, 5), facecolor=_GRID)

    ax.set_facecolor(_GRID)

    # Decision boundary cross-hairs
    ax.axhline(0, color=_ACCENT, linewidth=0.6, alpha=0.5)
    ax.axvline(0, color=_ACCENT, linewidth=0.6, alpha=0.5)

    # Noisy cloud
    if rx_symbols is not None:
        n = min(len(rx_symbols), max_points)
        idx = np.random.choice(len(rx_symbols), n, replace=False)
        ax.scatter(
            rx_symbols[idx].real, rx_symbols[idx].imag,
            s=4, alpha=0.35, color=_NOISY, label="Received",
        )

    # Ideal points (unique only)
    unique = np.unique(tx_symbols)
    ax.scatter(
        unique.real, unique.imag,
        s=80, zorder=5, color=_CLEAN, edgecolors="white", linewidths=0.6,
        label="Ideal",
    )

    ax.set_title(title, color=_TEXT, fontsize=11, pad=8)
    ax.tick_params(colors=_TEXT, labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor("#444455")
    ax.set_xlabel("In-phase (I)", color=_TEXT, fontsize=8)
    ax.set_ylabel("Quadrature (Q)", color=_TEXT, fontsize=8)
    ax.legend(fontsize=8, facecolor="#2A2A3E", labelcolor=_TEXT, framealpha=0.7)

    if standalone:
        plt.tight_layout()

    return ax


def plot_constellation_comparison(
    schemes: list[dict],
    snr_db: float,
    save_path: str | None = None,
) -> plt.Figure:
    """
    Multi-panel constellation comparison (clean vs noisy) for several schemes.

    Parameters
    ----------
    schemes : list of dicts with keys:
              'name'        – label
              'tx_symbols'  – ideal symbols
              'rx_symbols'  – received symbols (after AWGN)
    snr_db  : float – SNR used (for suptitle).
    save_path : optional file path to save the figure.
    """
    n = len(schemes)
    fig = plt.figure(figsize=(5 * n, 5), facecolor=_GRID)
    gs  = gridspec.GridSpec(1, n, figure=fig, wspace=0.3)

    for i, s in enumerate(schemes):
        ax = fig.add_subplot(gs[i])
        plot_constellation(
            s["tx_symbols"], s["rx_symbols"],
            title=s["name"], ax=ax,
        )

    fig.suptitle(
        f"Constellation Diagrams  –  SNR = {snr_db:.0f} dB",
        color=_TEXT, fontsize=13, y=1.02,
    )

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight", facecolor=_GRID)

    return fig
