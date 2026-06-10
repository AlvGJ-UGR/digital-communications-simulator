# Key Equations Reference

## Channel Model

```
r(t) = s(t) + n(t)
```

## SNR Definitions

```
SNR_symbol  =  Es / N0
SNR_bit     =  Eb / N0  =  Es / (N0 · log2(M))
```

## BER Formulas

| Scheme    | BER Expression |
|-----------|---------------|
| BPSK      | `Q(√(2·Eb/N0))` |
| QPSK      | `Q(√(2·Eb/N0))` |
| 16-QAM    | `(3/4)·Q(√(8/5 · Eb/N0))` (approx) |
| M-QAM     | `(4/log2(M))·(1−1/√M)·Q(√(3·log2(M)·Eb/N0/(M−1)))` |

## Q-Function

```
Q(x) = (1/2) · erfc(x / √2)
```

## AWGN Noise Power

```
σ²  =  P_signal / SNR_linear
σ²  =  P_signal / 10^(SNR_dB / 10)
```

For complex noise:
```
n = σ/√2 · (n_I + j·n_Q),    n_I, n_Q ~ N(0,1)
```

## Normalisation — Square M-QAM

```
E_avg  =  (2/3) · (M − 1) · d²_min
norm   =  √E_avg
```

## Spectral Efficiency

```
η  =  log2(M)    [bits / symbol / Hz]
```
