# Contributing

Thank you for considering a contribution to **digital-communications-simulator**.

---

## Getting started

1. **Fork** the repository and clone your fork.
2. Create a feature branch: `git checkout -b feature/your-topic`.
3. Install dev dependencies: `pip install -r requirements.txt`.
4. Make your changes and confirm `python main.py` runs cleanly.
5. Open a **pull request** against `main` with a clear description of what changed and why.

---

## Repo layout policy

| Location | What goes there |
|----------|----------------|
| `src/` | Core library modules (modulation, channel, detection, metrics) |
| `simulations/` | Scripts that run experiments and save figures |
| `results/plots/` | Generated figures — **git-ignored**, never commit these |
| `docs/` | Theory and reference documentation |

---

## Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Every public function must have a NumPy-style docstring with **Parameters** and **Returns** sections.
- Prefer `numpy` vectorised operations over Python loops where possible.
- Keep each module focused on a single responsibility.

---

## Areas where help is especially welcome

- **OFDM** — multicarrier extension with cyclic prefix
- **Turbo / LDPC / Polar codes** — FEC to show coding gain on BER curves
- **Soft-decision (LLR) demodulators** — needed by any coded system
- **Streamlit / Dash GUI** — interactive SNR slider, live BER and constellation
- **Unit tests** — `pytest` suite covering modulators, demodulators, and BER math

---

## Opening issues

Please use the GitHub issue tracker for:

- Bug reports (include a minimal reproducer)
- Feature requests (describe the use case, not just the implementation)
- Questions about the theory or the code
