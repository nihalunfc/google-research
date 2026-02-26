import json
from datetime import datetime

class MedChronMapper:
    """
    Simulates mapping raw OS-level signals (Android UsageStats / Laptop CPU) 
    into a structured FHIR-lite format for MedGemma 1.5.
    """
    
    def __init__(self):
        self.observation_type = "BehavioralPhenotype"

    def map_android_usage(self, raw_usage_stats):
        """Maps Android 'UsageStatsManager' data to Cognitive Load markers."""
        # In a real app, this would iterate through actual package usage
        total_switches = raw_usage_stats.get("app_launches", 0)
        
        return {
            "category": "CognitiveLoad",
            "metric": "AppSwitchingDensity",
            "value": total_switches,
            "interpretation": "High" if total_switches > 15 else "Normal"
        }

    def map_sleep_segment(self, inactivity_data):
        """Maps 'Device Inactivity' bins to Sleep Fragmentation markers."""
        # Simulated logic for detecting screen-on events during rest hours
        is_fragmented = inactivity_data.get("screen_on_count_midnight_to_5am", 0) > 0
        
        return {
            "category": "CircadianRhythm",
            "metric": "SleepFragmentation",
            "status": "Fragmented" if is_fragmented else "Stable"
        }

    def finalize_payload(self, android_data, laptop_data):
        """Creates the final JSON payload for the Inference Engine."""
        payload = {
            "source": "MedChron_Central_Hub",
            "timestamp": str(datetime.now()),
            "observations": [
                self.map_android_usage(android_data),
                self.map_sleep_segment(android_data)
            ],
            "system_signals": {
                "laptop_thermal_load": laptop_data.get("cpu_temp", "Normal"),
                "active_work_hours": laptop_data.get("sustained_usage_hours", 0)
            }
        }
        return payload

# Example usage for the GitHub repo
if __name__ == "__main__":
    mapper = MedChronMapper()
    
    # Mock data coming from a phone and laptop
    mock_phone = {"app_launches": 22, "screen_on_count_midnight_to_5am": 4}
    mock_laptop = {"cpu_temp": "High", "sustained_usage_hours": 6}
    
    final_json = mapper.finalize_payload(mock_phone, mock_laptop)
    print(json.dumps(final_json, indent=4))
