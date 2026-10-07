# Checks if a processing activity has a valid legal basis, following arts. 7 and 11.

BASES = {
    "consent",
    "legal_obligation",
    "public_policy",
    "research",
    "contract",
    "legal_process",
    "life_protection",
    "health",
    "legitimate_interest",
    "credit_protection",
}

# these two can't be used for sensitive data
NOT_FOR_SENSITIVE = {"legitimate_interest", "credit_protection"}


def check_activity(purpose, basis, sensitive=False):
    if basis not in BASES:
        return False, f"'{basis}' is not a legal basis"
    if sensitive and basis in NOT_FOR_SENSITIVE:
        return False, f"'{basis}' can't be used for sensitive data"
    return True, f"ok: {purpose} -> {basis}"


if __name__ == "__main__":
    activities = [
        ("send newsletter", "consent", False),
        ("issue invoice", "legal_obligation", False),
        ("marketing with health data", "legitimate_interest", True),
        ("fingerprint at the gym door", "consent", True),
        ("sell customer list", "because_we_want", False),
    ]
    for purpose, basis, sensitive in activities:
        ok, message = check_activity(purpose, basis, sensitive)
        print("OK " if ok else "NO ", message)
