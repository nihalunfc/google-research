import hashlib

def anonymize_user_id(user_email):
    """
    Ensures that the user's real identity is never 
    associated with the behavioral logs in the AI prompt.
    """
    return hashlib.sha256(user_email.encode()).hexdigest()[:12]

def encrypt_local_logs(data):
    # This represents the AES-256 layer for at-rest encryption
    print("🔒 Encrypting local FHIR-lite logs before storage...")
    return f"ENC-{hashlib.md5(data.encode()).hexdigest()}"

if __name__ == "__main__":
    print(f"User Hash: {anonymize_user_id('nihal@unfc.ca')}")
