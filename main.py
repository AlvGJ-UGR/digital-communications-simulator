"""
main.py
-------
Entry point for the Digital Communications Simulator.

Runs all simulations in sequence and saves results to results/plots/.

Usage
-----
    python main.py              # full run
    python main.py --quick      # reduced sample count (faster demo)
    python main.py --only ber   # run only BER simulation
    python main.py --only const # run only constellation simulation
"""

import argparse
import os
import sys
import time

# ── make sure the project root is on the path ───────────────────────────────
ROOT = os.path.dirname(__file__)
sys.path.insert(0, ROOT)

from simulations.ber_vs_snr           import run as run_ber
from simulations.constellation_examples import (
    plot_clean_noisy, plot_snr_sweep,
)

BANNER = r"""
╔══════════════════════════════════════════════════════╗
║   Digital Communications Simulator                  ║
║   BPSK · QPSK · 16-QAM · 64-QAM  |  AWGN Channel   ║
╚══════════════════════════════════════════════════════╝
"""


def main():
    parser = argparse.ArgumentParser(description="Digital Communications Simulator")
    parser.add_argument("--only",  choices=["ber", "const"], default=None,
                        help="Run only one simulation module.")
    parser.add_argument("--quick", action="store_true",
                        help="Reduce sample count for a faster demo run.")
    args = parser.parse_args()

    print(BANNER)
    os.makedirs(os.path.join(ROOT, "results", "plots"), exist_ok=True)

    t0 = time.time()

    run_ber_flag   = args.only in (None, "ber")
    run_const_flag = args.only in (None, "const")

    if run_ber_flag:
        print("── BER vs Eb/N0 simulation ──────────────────────────")
        run_ber(save=True)

    if run_const_flag:
        print("\n── Constellation diagrams ───────────────────────────")
        print("  Generating clean vs noisy  (SNR = 10 dB) …")
        plot_clean_noisy(snr_db=10, save=True)
        print("  Generating SNR sweep for 16-QAM …")
        plot_snr_sweep("16-QAM", save=True)

    elapsed = time.time() - t0
    print(f"\n✓  All simulations complete in {elapsed:.1f}s")
    print(f"   Plots saved to  →  {os.path.join(ROOT, 'results', 'plots')}/")


if __name__ == "__main__":
    main()
