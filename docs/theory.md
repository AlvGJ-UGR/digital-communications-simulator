# Theory of Digital Modulation

## 1. System Model

The complete communication chain simulated in this project follows the standard discrete-time baseband model:

```
b[n] ──► Mapper ──► s[n] ──► + n[n] ──► r[n] ──► Detector ──► b̂[n]
                                ↑
                              n[n] ~ CN(0, σ²)
```

Where:
- `b[n]`  — transmitted bit sequence
- `s[n]`  — complex baseband symbols (after mapping)
- `n[n]`  — complex AWGN noise
- `r[n]`  — received signal
- `b̂[n]` — detected (decoded) bits

---

## 2. AWGN Channel

The Additive White Gaussian Noise channel is the fundamental benchmark model in digital communications. The received signal is:

```
r(t) = s(t) + n(t)
```

The noise `n(t)` is a zero-mean, wide-sense stationary Gaussian random process with power spectral density `N₀/2` W/Hz (two-sided).

For a complex baseband signal, the noise is split equally between I and Q:
- `n_I ~ N(0, σ²/2)`
- `n_Q ~ N(0, σ²/2)`

So total noise power is `σ² = N₀/2 · B` for bandwidth `B`.

---

## 3. Signal-to-Noise Ratio

The key figure of merit is **Eb/N0** (energy per bit to noise spectral density ratio), expressed in dB:

```
Eb/N0 [dB] = 10 · log10(Eb / N0)
```

Relationship to symbol SNR (Es/N0):

```
Es/N0 = Eb/N0 · log2(M)
```

where `M` is the constellation size.

---

## 4. Modulation Schemes

### 4.1 BPSK — Binary Phase-Shift Keying

The simplest digital modulation. One bit maps to one of two antipodal symbols:

```
0 → s = -1    (phase = π)
1 → s = +1    (phase = 0)
```

The decision boundary is the imaginary axis (Re{r} = 0).

**Theoretical BER:**
```
BER_BPSK = Q(√(2·Eb/N0))
```

---

### 4.2 QPSK — Quadrature Phase-Shift Keying

Two bits per symbol, Gray-coded. The constellation has 4 points at ±45°, ±135°:

```
00 → +1+j   01 → -1+j
10 → +1-j   11 → -1-j
```

Normalised to unit energy: divide by √2.

QPSK achieves **twice the spectral efficiency** of BPSK with identical BER performance (as a function of Eb/N0), because the decision regions for I and Q are independent.

**Theoretical BER:**
```
BER_QPSK = Q(√(2·Eb/N0))
```

---

### 4.3 M-QAM — Quadrature Amplitude Modulation

Combines amplitude and phase modulation. For square constellations (M = 4, 16, 64, 256, …):

- log2(M) bits per symbol
- I and Q components each carry log2(√M) bits
- Gray coding applied independently to each axis

**Average symbol energy normalisation:**
```
E_avg = (M-1) · 2/(3) · d²min
```

where `d_min` is the minimum inter-symbol distance. We normalise so `E_avg = 1`.

**Approximate theoretical BER (Gray-coded square M-QAM):**
```
BER ≈ (4/log2(M)) · (1 - 1/√M) · Q(√(3·log2(M)·Eb/N0 / (M-1)))
```

---

## 5. The Q-Function

The Q-function is the tail probability of the standard normal distribution:

```
Q(x) = (1/√(2π)) ∫_x^∞ exp(-t²/2) dt = (1/2) · erfc(x/√2)
```

It appears in all BER expressions because detection errors occur when Gaussian noise pushes a received sample past the decision boundary.

---

## 6. Spectral Efficiency

| Scheme   | M    | bits/symbol | Relative bandwidth |
|----------|------|-------------|-------------------|
| BPSK     | 2    | 1           | 1× (baseline)     |
| QPSK     | 4    | 2           | ½                 |
| 8-PSK    | 8    | 3           | ⅓                 |
| 16-QAM   | 16   | 4           | ¼                 |
| 64-QAM   | 64   | 6           | ⅙                 |
| 256-QAM  | 256  | 8           | ⅛                 |

Higher-order constellations pack more bits per symbol (higher spectral efficiency) at the cost of reduced noise margin (lower BER performance at the same Eb/N0).

---

## 7. Rayleigh Fading

In multipath-rich environments without a line-of-sight component, the channel amplitude follows a Rayleigh distribution. Each symbol is multiplied by an independent complex Gaussian coefficient:

```
h ~ CN(0, 1)     i.e.   h = (h_I + j·h_Q) / √2,   h_I, h_Q ~ N(0,1)
```

The received signal becomes:
```
r[n] = h[n] · s[n] + w[n]
```

With perfect channel state information (CSI), a zero-forcing equaliser recovers:
```
ŝ[n] = r[n] / h[n]
```

Unlike AWGN, Rayleigh fading introduces a **BER floor** at high SNR due to deep fades — the core motivation for diversity techniques in real systems.
