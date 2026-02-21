# 🏥 MedChron: Personal Medical Narrative AI
### Google MedGemma Impact Challenge | Kaggle 2026

**MedChron** is a stylish, privacy-first application designed to transform fragmented health data into a cohesive longitudinal medical narrative. Built using **Google’s MedGemma 1.5** and the **HAI-DEF** ecosystem, it bridges the gap between patient-logged symptoms and actionable clinical insights.

---

## 🚀 Project Vision
Healthcare is often a series of snapshots. **MedChron** provides the "film"—a continuous, AI-reasoned record of a patient's health journey. This is particularly vital for communities managing chronic conditions or navigating new healthcare systems (like international students and immigrants in Canada).

### Key Features
* **Longitudinal Reasoning:** Powered by MedGemma 1.5 to correlate recovery times and symptom intensity over months, not just days.
* **Vitals & Wearable Hub:** Seamlessly integrates Resting Heart Rate (RHR), sleep, and activity data to detect physiological "noise" before symptoms peak.
* **FemTech Integration:** Specialized tracking for menstrual cycles and PCOD/PCOS symptoms, utilizing AI to apply the Rotterdam Criteria for decision support.
* **The "Vault" (Edge AI):** Local inference via **MedGemma 1.5 4B** ensures that sensitive medical data never leaves the user's device.

---

## 🛠️ Technical Stack
* **Core Model:** `google/medgemma-1.5-4b-it` (Multimodal Medical Reasoning)
* **Personalization:** `Gemini 1.5 Pro` (Adaptive user interface & peer-like support)
* **Data Hub:** FHIR-lite (Fast Healthcare Interoperability Resources)
* **Security:** AES-256 Local Encryption & E2EE sharing protocols
* **Environment:** Kaggle Notebooks (Dual T4 GPU) & GitHub

---

## 📂 Repository Structure
```text
├── notebooks/          # Kaggle Notebook exports (.ipynb)
├── src/                # Inference engines & clinical NLP modules
├── data/               # FHIR-compliant synthetic health generators
└── docs/               # Technical write-up & MedChron Brand Assets
