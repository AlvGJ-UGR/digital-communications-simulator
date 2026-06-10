# 📡 Digital Communication System Simulator

Simulador completo de un sistema de comunicaciones digitales que implementa modulaciones básicas (BPSK, QPSK y M-QAM), canal AWGN y análisis de BER (Bit Error Rate).

Este proyecto está orientado a telecomunicaciones digitales, procesamiento de señales y simulación de canales.

---

## 🎯 Objetivo

Simular un sistema de transmisión digital completo:

Bits → Modulación → Canal AWGN → Demodulación → BER

El objetivo es comparar el rendimiento de diferentes esquemas de modulación bajo distintas condiciones de SNR.

---

## ⚙️ Características

- Generación de bits aleatorios
- Modulaciones implementadas:
  - BPSK
  - QPSK
  - 16-QAM
- Canal AWGN (Additive White Gaussian Noise)
- Demodulación coherente
- Cálculo de BER
- Análisis BER vs SNR
- Diagramas de constelación
- Comparación de eficiencia espectral

---

## 📊 Resultados esperados

El proyecto permite visualizar:

- Curvas BER vs SNR
- Constelaciones con y sin ruido
- Comparación entre modulaciones

---

## 🧠 Fundamento teórico

El sistema modela un canal AWGN:

r(t) = s(t) + n(t)

donde:
- s(t): señal transmitida
- n(t): ruido gaussiano blanco

La métrica principal es el BER:

BER = número de bits erróneos / total de bits transmitidos

---

## 📁 Estructura del proyecto
digital-communications-simulator/
│
├── src/
│ ├── modulation/
│ ├── demodulation/
│ ├── channel/
│ ├── metrics/
│ ├── utils/
│
├── simulations/
├── docs/
├── results/
├── main.py
└── README.md

---


# 📡 Modelo del sistema

El canal se modela como:

r(t) = s(t) + n(t)

donde:
- s(t): señal transmitida
- n(t): ruido gaussiano blanco

---

# 📶 Modulaciones implementadas

## BPSK
- 1 bit por símbolo
- Alta robustez al ruido

## QPSK
- 2 bits por símbolo
- Compromiso entre eficiencia y robustez

## 16-QAM
- 4 bits por símbolo
- Alta eficiencia espectral, más sensible al ruido

---

# 📉 Resultados esperados

El proyecto genera:

- Curvas BER vs SNR
- Diagramas de constelación
- Comparación entre modulaciones
- Análisis de robustez del sistema

---

# 📈 Ejemplo de análisis

- BPSK → mejor rendimiento en bajo SNR
- QPSK → equilibrio entre velocidad y robustez
- 16-QAM → mayor velocidad, más errores en ruido

---

# 🧪 Posibles mejoras (nivel avanzado)

- Canal con fading (Rayleigh / Rician)
- OFDM (base de WiFi / LTE / 5G)
- Codificación de canal (Hamming, convolutional, LDPC)
- Sincronización de portadora y símbolo
- Interfaz gráfica (Streamlit o Dash)
- Simulación tipo SDR (Software Defined Radio)

---

# 🚀 Cómo ejecutar

```bash
pip install -r requirements.txt
python main.py



