# 📡 Digital Communications System Simulator

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-green.svg)
![Domain](https://img.shields.io/badge/Domain-Telecommunications%20%7C%20RF%20Engineering-orange.svg)

---

## 🧠 Overview

This project implements a **link-level digital communication system simulator**, modeling how information is transmitted over a real wireless channel under noise, interference, and propagation effects.

It replicates the core behavior of real-world systems such as:

- 📶 WiFi (802.11)
- 📡 LTE / 5G
- 🛰️ Satellite communications
- 📻 General RF communication systems

---

## 🎯 Objective

To analyze the performance of different digital modulation schemes under realistic channel conditions by evaluating:

- Bit Error Rate (BER)
- Signal-to-Noise Ratio (SNR)
- Symbol constellations
- Spectral efficiency trade-offs

---

## 🔁 System Architecture

The communication chain is modeled as:
Bits
→ Modulation
→ Pulse Shaping
→ Wireless Channel (AWGN + Fading + Path Loss)
→ Receiver Front-End
→ Demodulation
→ Decision Logic
→ BER Evaluation

---

## 📡 Channel Model

The wireless channel is modeled as:

r(t) = s(t) + n(t)

Where:
- s(t): transmitted signal
- n(t): additive white Gaussian noise

Advanced extensions include:

- 🌪 Rayleigh / Rician fading
- 📉 Path loss modeling
- 🌫 Shadowing effects
- 📡 Multipath propagation

---

## 📶 Modulation Schemes Implemented

### BPSK
- 1 bit/symbol
- Maximum robustness
- Low spectral efficiency

### QPSK
- 2 bits/symbol
- Balanced performance

### 16-QAM
- 4 bits/symbol
- High spectral efficiency
- More sensitive to noise

---

## 📊 Key Performance Metrics

### Bit Error Rate (BER)

BER = number of erroneous bits / total transmitted bits

---

### Signal-to-Noise Ratio (SNR)

SNR = Eb / N0

---

### Error Vector Magnitude (EVM)

EVM = sqrt( E[|s - r|²] / E[|s|²] )

---

### Channel Capacity (Shannon Limit)

C = B log2(1 + SNR)

---

## 📈 Expected Results

The simulator generates:

- 📉 BER vs SNR curves (log scale)
- 📡 Constellation diagrams (ideal vs noisy)
- 📊 Modulation comparison charts
- ⚖️ Trade-off analysis (robustness vs efficiency)

---

## 🧪 Engineering Insights

This project demonstrates:

- Digital communication system design
- RF channel modeling
- Statistical signal processing
- Monte Carlo simulation techniques
- Trade-off analysis in wireless systems

---

## 🧱 Project Structure

```text
digital-communications-simulator/
│
├── src/
│   ├── modulation/
│   ├── demodulation/
│   ├── channel/
│   ├── coding/
│   ├── metrics/
│   ├── utils/
│
├── simulations/
│   ├── ber_vs_snr.py
│   ├── constellation_analysis.py
│
├── docs/
│   ├── theory.md
│   ├── rf_models.md
│   ├── equations.md
│
├── results/
│   ├── plots/
│
├── main.py
├── config.yaml
├── requirements.txt
└── README.md
