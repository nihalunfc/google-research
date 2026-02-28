# MedChron: Passive Mental Health Phenotyping
### Edge-AI Behavioral Analysis Engine | Research Prototype

MedChron is a privacy-first behavioral analysis platform designed to transform "digital exhaust"—passive device telemetry—into actionable mental health insights. By leveraging local execution of **Google’s MedGemma 1.5**, the system detects shifts in circadian rhythms, cognitive load, and burnout risk without requiring active user input.

> **Note on Submission:** This project was developed for the **Google MedGemma Impact Challenge (2026)**. Although the official submission window closed prior to final completion, the project was fully realized as a research prototype to demonstrate the potential of medical LLMs in passive sensing.

---

## Project Objectives
* **Eliminate Self-Reporting Bias**: Move from subjective user surveys to objective "Digital Phenotyping" based on device usage patterns.
* **Privacy-First Architecture**: Utilize Edge AI to ensure sensitive behavioral data is processed locally, never leaving the user's environment.
* **Longitudinal Reasoning**: Use MedGemma’s medical reasoning capabilities to correlate fragmented sleep with daytime cognitive performance.

---

## Technical Stack & Services
* **Core Model**: `google/medgemma-1.5-4b-it` (Specialized in longitudinal behavioral reasoning).
* **Compute**: Kaggle Dual T4 GPU environment.
* **Quantization**: 4-bit NormalFloat (NF4) via `bitsandbytes` to optimize for edge hardware.
* **Inference**: Hugging Face Transformers & Accelerate (Device mapping for dual-GPU load balancing).
* **Data Standard**: FHIR-lite behavioral observation structures.
* **UI Layer**: Streamlit (Python-based dashboard prototyping).

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

## File Manifest and Descriptions

### Data Layer (/data)
* **full_loop_data.json**: Contains 1,440 minutes of simulated telemetry, including app-switch density, phone screen-on events, and laptop CPU utilization.
* **ui_snapshot.json**: The processed result from the AI, containing the "Live Narrative" and calculated burnout risk status.

### Documentation Layer (/docs)
* **ARCHITECTURE.md**: Details the three-tier system: Ingestion (Mobile/PC), Processing (MedGemma), and Visualization (Streamlit).
* **PRIVACY.md**: Outlines the ethical safeguards, specifically the "Local-Only" processing mandate to protect user medical data.

### Source Code Layer (/src)
* **full_loop_inference.py**: The primary execution script. It generates a fresh data cycle, loads the model in 4-bit, and generates the mental health report.
* **data_mapper.py**: Acts as the "translator" between raw hardware signals and high-level concepts (e.g., converting app launches into "Cognitive Load").
* **security_vault.py**: Implements SHA-256 hashing for user anonymization to ensure the AI reasoning engine never sees a user's real name.

---

## How the System Works: Technical Logic

1. **Passive Ingestion**: The system monitors "Device Inactivity Bins" on mobile to infer sleep segments and tracks "Application Switching Density" on the laptop to measure multitasking intensity.
2. **Signal Normalization**: `data_mapper.py` aggregates these raw signals into an AI-ready prompt, framing the data within a clinical context.
3. **Local Reasoning**: MedGemma 1.5 4B processes the prompt. Using its medical training, it identifies anomalies—such as phone usage during typical REM cycles or sustained high-CPU usage during rest hours.
4. **Insight Generation**: The engine outputs a "MedChron Live Report" which categorizes the user's current behavioral state.

---

## Setup and Execution Guide

To reproduce this project in a Kaggle or local GPU environment:

### 1. Environment Requirements
* **GPU**: Minimum 12GB VRAM (T4 or higher recommended).
* **Hugging Face Access**: You must be authorized to use the gated `google/medgemma-1.5-4b-it` model.
* **Kaggle Secrets**: Store your Hugging Face token as a secret named `HF_TOKEN`.

### 2. Dependency Installation
```python
!pip install -q -U bitsandbytes>=0.46.1 transformers accelerate
```

*Note: A session restart is mandatory after installation to initialize the updated bitsandbytes library.*

### 3. Running the Full Pipeline

Navigate to the `src/` directory and execute the inference script:

```bash
python src/full_loop_inference.py

```

This will generate the synthetic logs, load the quantized weights, and produce the final `ui_snapshot.json` file.

```
## Full Repository Structure

.
├── data/
│   ├── digital_phenotype_logs.json # Initial passive sensing data simulator
│   ├── full_loop_data.json         # Master 24-hour activity logs (Input)
│   └── ui_snapshot.json            # AI-generated report for dashboard (Output)
├── docs/
│   ├── ARCHITECTURE.md             # Technical system design and data ingestion layers
│   ├── PRIVACY.md                  # Ethics, data minimization, and zero-knowledge framework
│   ├── inference_sample.md         # Raw logs of MedGemma reasoning chains
│   └── sample_output.md            # Formatted MedChron Live Report
├── notebooks/
│   └── medchron_analysis.ipynb     # Full Kaggle notebook with end-to-end execution
├── src/
│   ├── data_mapper.py              # Normalizes raw OS signals into AI-ready structures
│   ├── full_loop_inference.py      # End-to-end pipeline execution script
│   ├── inference_engine.py         # Module for MedGemma analysis and engine setup
│   ├── security_vault.py           # User ID anonymization and log encryption logic
│   └── ui_dashboard.py             # Streamlit prototype for mental health reporting
└── README.md                       # Primary project documentation



