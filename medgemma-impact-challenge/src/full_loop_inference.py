import os
import torch
import json
from datetime import datetime
from kaggle_secrets import UserSecretsClient
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# --- PHASE 1: AUTHENTICATION ---
user_secrets = UserSecretsClient()
hf_token = user_secrets.get_secret("HF_TOKEN")
login(token=hf_token)

# --- PHASE 2: DATA GENERATION (The Digital Phenotype) ---
def generate_fresh_logs():
    print("📊 Phase 1: Generating raw device activity logs...")
    data = {"user_id": "nihal_unf_student", "activity_logs": []}
    # Simulating a high-stress day with 4 hours of late-night laptop work
    for h in range(24):
        is_active = True if (1 <= h <= 3) or (9 <= h <= 23) else False
        switches = 15 if (10 <= h <= 15) else 3
        cpu = 90 if (21 <= h <= 23) else 20
        data["activity_logs"].append({
            "timestamp": f"{h:02d}:00",
            "phone_active": is_active,
            "app_switches": switches,
            "laptop_cpu": cpu
        })
    with open('full_loop_data.json', 'w') as f:
        json.dump(data, f)
    return 'full_loop_data.json'

log_file = generate_fresh_logs()

# --- PHASE 3: LOAD MEDGEMMA 1.5 ---
model_id = "google/medgemma-1.5-4b-it"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

print(f"🧠 Phase 2: Loading MedGemma 1.5 for reasoning...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, quantization_config=bnb_config, device_map="auto"
)

# --- PHASE 4: THE REASONING LOOP ---
def run_inference(file_path):
    with open(file_path, 'r') as f:
        logs = json.load(f)['activity_logs']
    
    # Extract markers for the prompt
    night_usage = [l['timestamp'] for l in logs if l['phone_active'] and "01:00" <= l['timestamp'] <= "04:00"]
    
    prompt = f"""<start_of_turn>user
    Identify mental health risks from these digital biomarkers:
    - User was on phone during typical sleep hours at: {night_usage}
    - Laptop CPU was at 90% capacity from 10 PM to Midnight.
    - App switching frequency is 3x higher than baseline during morning hours.
    
    Provide a professional MedChron Live Report.<end_of_turn>
    <start_of_turn>model"""

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=350, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print("📝 Phase 3: Analyzing patterns...")
final_report = run_inference(log_file)

# --- PHASE 5: SAVE FOR UI ---
print("🖥️ Phase 4: Finalizing UI Snapshot...")
ui_output = {
    "report_text": final_report,
    "status": "Burnout Risk: High",
    "last_updated": str(datetime.now())
}
with open('ui_snapshot.json', 'w') as f:
    json.dump(ui_output, f, indent=4)

print("\n" + "="*30)
print("🚀 FULL LOOP COMPLETE")
print(final_report)
print("="*30)
