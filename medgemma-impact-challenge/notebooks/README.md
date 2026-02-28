# MedChron: Analysis Notebooks

This directory contains the primary research and development notebook for the MedChron prototype. It captures the iterative process of model selection, quantization testing, and inference validation.

## Notebook Manifest

### medchron_analysis.ipynb
This is the primary end-to-end execution notebook designed for the **Kaggle GPU T4 x2** environment. It serves as the master orchestration for the following phases:

1.  **Environment Setup**: Force-upgrading `bitsandbytes`, `transformers`, and `accelerate` to support MedGemma 1.5 4-bit quantization.
2.  **Synthetic Data Generation**: Creating the initial 24-hour behavioral phenotype logs.
3.  **Model Loading**: Authenticating with Hugging Face and loading `google/medgemma-1.5-4b-it` with NF4 quantization.
4.  **Clinical Reasoning**: Executing the inference loop to generate mental health reports based on device telemetry.
5.  **Artifact Generation**: Saving the final `full_loop_data.json` and `ui_snapshot.json` for repository documentation.

## How to use this folder

To reproduce the analysis, upload the `.ipynb` file to a new Kaggle Notebook and follow the **Setup and Execution Guide** provided in the primary repository README. Ensure that your **Hugging Face Token** is added to the Kaggle Secrets tab before execution.
