# Pseudonymization vs anonymization, from module 1 and 3.
# Pseudonymized data can be linked back (whoever has the key can), so it's still personal data.

import hashlib
import hmac

SECRET_KEY = b"keep-this-out-of-the-repo-in-real-life"


def pseudonymize_cpf(cpf):
    digits = cpf.replace(".", "").replace("-", "")
    return hmac.new(SECRET_KEY, digits.encode(), hashlib.sha256).hexdigest()[:16]


def mask_cpf(cpf):
    digits = cpf.replace(".", "").replace("-", "")
    return "***." + digits[3:6] + "." + digits[6:9] + "-**"


def anonymize_age(birth_year, current_year=2026):
    # turning an exact value into a range makes it much harder to identify someone
    age = current_year - birth_year
    start = age // 10 * 10
    return f"{start}-{start + 9}"


if __name__ == "__main__":
    customers = [
        {"name": "Ana Souza", "cpf": "123.456.789-09", "birth_year": 1998},
        {"name": "Bruno Lima", "cpf": "987.654.321-00", "birth_year": 1985},
    ]
    for c in customers:
        print(pseudonymize_cpf(c["cpf"]), mask_cpf(c["cpf"]), anonymize_age(c["birth_year"]))
