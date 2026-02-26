import os
import torch
import json
from kaggle_secrets import UserSecretsClient
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# 1. Authenticate (Ensure HF_TOKEN is enabled in Add-ons -> Secrets)
user_secrets = UserSecretsClient()
hf_token = user_secrets.get_secret("HF_TOKEN")
login(token=hf_token)

# 2. Precise Model ID from Hugging Face
model_id = "google/medgemma-1.5-4b-it"

# 3. 4-bit Config (Optimized for your Dual T4 GPUs)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True
)

# 4. Load Model & Tokenizer
print(f" Initializing download for {model_id}...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True
)
print(" MedGemma 1.5 is now loaded in 4-bit VRAM!")

# 5. MedChron Analysis Function
def run_medchron_analysis(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Extracting patterns for the AI to reason over
    logs = data['activity_logs']
    # Filtering for phone activity between 1 AM and 5 AM
    late_night = [l['timestamp'] for l in logs if l['phone_active'] and "01:00" <= l['timestamp'] <= "05:00"]
    # Filtering for high app switching
    high_switching = [l['timestamp'] for l in logs if l['app_switches'] > 12]

    # Creating a medical-style prompt
    prompt = f"""<start_of_turn>user
    You are a specialist in Digital Phenotyping and Behavioral Health. 
    Analyze the following device usage metadata for a single 24-hour period:
    
    - Observed sleep fragmentation (Phone active during rest hours): {late_night[:8]}
    - High cognitive load spikes (App switching >12/min): {high_switching[:8]}
    - Sustained laptop CPU usage (>80%) detected during late-evening hours.

    Based on these digital biomarkers, provide a professional 'MedChron Live Report'. 
    Discuss the user's circadian rhythm disruption, potential cognitive fatigue, and burnout risk.<end_of_turn>
    <start_of_turn>model"""

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    
    # Generate response
    outputs = model.generate(
        **inputs, 
        max_new_tokens=400, 
        temperature=0.7, 
        do_sample=True
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 6. Execute if data is ready
# Check if the file exists in the current directory
file_path = 'digital_phenotype_logs.json'
if os.path.exists(file_path):
    print("\n---  Generating MedChron Analysis ---")
    report = run_medchron_analysis(file_path)
    print("\n" + "="*50)
    print(report)
    print("="*50)
else:
    print(f" Error: {file_path} not found in {os.getcwd()}")
