# Tracks data subject requests (art. 18) and the 15 day deadline for complete answers (art. 19).

from datetime import date, timedelta

REQUEST_TYPES = [
    "confirmation",
    "access",
    "correction",
    "anonymization",
    "portability",
    "deletion",
    "sharing_info",
    "revoke_consent",
]

DEADLINE_DAYS = 15


class SubjectRequest:
    def __init__(self, subject, kind, opened_on):
        if kind not in REQUEST_TYPES:
            raise ValueError(f"unknown request type: {kind}")
        self.subject = subject
        self.kind = kind
        self.opened_on = opened_on
        self.answered = False

    def deadline(self):
        return self.opened_on + timedelta(days=DEADLINE_DAYS)

    def is_late(self, today):
        return not self.answered and today > self.deadline()

    def __str__(self):
        status = "answered" if self.answered else f"due {self.deadline()}"
        return f"{self.subject} - {self.kind} ({status})"


if __name__ == "__main__":
    today = date(2026, 10, 7)
    requests = [
        SubjectRequest("Ana", "access", date(2026, 9, 10)),
        SubjectRequest("Bruno", "deletion", date(2026, 10, 1)),
        SubjectRequest("Carla", "portability", date(2026, 9, 30)),
    ]
    requests[2].answered = True

    for r in requests:
        print(r, "<- LATE" if r.is_late(today) else "")
