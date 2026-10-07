# Flags which fields of a form/table would be personal or sensitive data under LGPD.
# Very simple keyword matching, just to practice the categories from module 1.

SENSITIVE_KEYWORDS = [
    "race", "ethnicity", "religion", "political", "union",
    "health", "disease", "sexual", "genetic", "biometric", "fingerprint", "blood",
]

PERSONAL_KEYWORDS = [
    "name", "cpf", "rg", "email", "phone", "address", "birth",
    "ip", "location", "plate",
]


def classify_field(field_name):
    name = field_name.lower()
    for word in SENSITIVE_KEYWORDS:
        if word in name:
            return "sensitive"
    for word in PERSONAL_KEYWORDS:
        if word in name:
            return "personal"
    return "not personal"


def classify_table(columns):
    return {column: classify_field(column) for column in columns}


if __name__ == "__main__":
    patient_table = ["full_name", "cpf", "birth_date", "health_plan", "blood_type", "room_number"]
    for column, kind in classify_table(patient_table).items():
        print(f"{column:<12} {kind}")
