# 🧠 MedChron: Passive Mental Health Phenotyping
### Google MedGemma Impact Challenge | Kaggle 2026

**MedChron** is a stylish, privacy-first behavioral analysis engine designed to transform personal device activity into live mental health insights. Built on **Google’s MedGemma 1.5**, it uses passive sensing to detect shifts in sleep patterns, cognitive load, and eye health without requiring any manual user input.

---

## 🚀 The Vision: Beyond Self-Reporting
Traditional mental health tracking is flawed because it relies on subjective self-reports. **MedChron** introduces **Digital Phenotyping**—using the "digital exhaust" of our daily lives as a biological signal:

* **Sleep Mapping via Inactivity:** Uses 15-minute "inactivity bins" on Android/iOS to infer deep rest periods and sleep hygiene without a wearable.
* **Cognitive Load Tracking:** Analyzes "App Switching Density" and laptop processing intensity to detect early signs of stress or burnout.
* **Centralized Device Repo:** Connects a single user’s data across mobile (Google Health Connect) and personal laptops via a secure Google Account integration.
* **Eye Health & Reset Alerts:** Monitors continuous screen exposure and ambient light to suggest "Brain Resets" and blue-light breaks.

---

## 🛠️ Technical Stack
* **Core AI Engine:** `google/medgemma-1.5-4b-it` (Specialized in longitudinal behavioral reasoning).
* **Personalization Layer:** **Gemini 1.5 Pro** (Converts raw data into empathetic, student-friendly live reports).
* **Data Standard:** FHIR-lite for cross-platform behavioral logs.
* **Compute:** Kaggle Notebooks (Dual T4 GPU) with 4-bit quantization via `bitsandbytes`.
* **Privacy:** **Edge AI Architecture** — behavioral analysis happens locally to ensure medical data is end-to-end encrypted and user-owned.

---
## 📈 Project Activity & Development Log
| Date | Milestone | Status | Technical Notes |
| :--- | :--- | :--- | :--- |
| **2026-02-20** | Project Pivot & Rebrand | ✅ | Shifted to Passive Mental Health Phenotyping (MedChron). |
| **2026-02-21** | Synthetic Data Hub | ✅ | Created FHIR-lite generator for behavioral time-series logs. |
| **2026-02-26** | MedGemma 1.5 Reasoning | ✅ | Successfully loaded 4-bit Quantized Model on Dual T4 GPUs. |
| **2026-02-27** | Data Hub Architecture | 🏗️ | Designing Google Health Connect & Cross-platform sync. |
| **2026-03-01** | UI Prototype | ⏳ | Planning Streamlit dashboard for "Live Mental Health Reports." |
---
## ✅ Project Status: Completed (Research Prototype)

| Date | Milestone | Status |
| :--- | :--- | :--- |
| **2026-02-28** | Full Loop Validation | ✅ **Success** |

### 🚀 Key Achievement
Successfully integrated **MedGemma 1.5 4B** (quantized to 4-bit) with a custom **Digital Phenotype Mapper**. The system correctly identified:
1. **Sleep Fragmentation:** Phone activity during biological rest hours (01:00-03:00).
2. **Burnout Markers:** Sustained 90% CPU load during late-evening hours.
3. **Anxiety Signals:** 3x baseline app-switching frequency during morning hours.

### 🛠️ Tech Stack
- **AI Model:** Google MedGemma 1.5 4B (Instruction Tuned)
- **Environment:** Kaggle Dual T4 GPU
- **Libraries:** Hugging Face Transformers, BitsAndBytes (4-bit NF4), PyTorch
- **Architecture:** Local-first / Zero-Knowledge Privacy Model

## 📂 Repository Structure
```text
├── docs/
│   ├── ARCHITECTURE.md       <-- (Paste the text above here)
│   └── sample_report.md      <-- (Paste your MedGemma output here)
├── src/
│   ├── data_generator.py     <-- (The script you ran to make the JSON)
│   └── inference_engine.py   <-- (The script that loads MedGemma)
├── data/
│   └── digital_phenotype.json <-- (The output from your generator)
└── README.md                 <-- (The main file with the Progress Log)
