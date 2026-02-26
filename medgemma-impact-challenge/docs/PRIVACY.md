# 🔒 MedChron: Privacy & Data Ethics Framework

MedChron operates on a **Zero-Knowledge** and **Local-First** philosophy.

### 1. Data Minimization
We do not track specific app content or message text. We only track "Meta-Patterns" (e.g., timestamps of activity, frequency of window switches).

### 2. Local-Only Reasoning
The **MedGemma 1.5** model runs locally on the user's hardware. 
- **No raw behavioral data** is sent to Google or MedChron servers.
- **Inference** happens on the Edge (Mobile/Laptop).

### 3. User Sovereignty
- Users own their "Digital Phenotype" data stored in their private Google Drive.
- MedChron acts only as a local interface to that data.
- Opt-out is immediate: Deleting the local cache stops all analysis.

### 4. Ethical Guardrails
MedChron is a **support tool**, not a diagnostic one. If the AI detects critical burnout or severe distress patterns, it is programmed to provide links to professional human resources rather than attempting a medical diagnosis.
