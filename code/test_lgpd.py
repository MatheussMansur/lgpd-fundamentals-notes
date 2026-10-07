import unittest

from legal_basis import check_activity
from pseudonymize import anonymize_age, mask_cpf, pseudonymize_cpf
from sensitive_fields import classify_field
from subject_requests import SubjectRequest
from datetime import date


class TestSensitiveFields(unittest.TestCase):
    def test_sensitive(self):
        self.assertEqual(classify_field("religion"), "sensitive")
        self.assertEqual(classify_field("blood_type"), "sensitive")

    def test_personal(self):
        self.assertEqual(classify_field("email_address"), "personal")

    def test_not_personal(self):
        self.assertEqual(classify_field("product_price"), "not personal")


class TestLegalBasis(unittest.TestCase):
    def test_consent_is_valid(self):
        self.assertTrue(check_activity("newsletter", "consent")[0])

    def test_unknown_basis(self):
        self.assertFalse(check_activity("x", "nope")[0])

    def test_legitimate_interest_not_for_sensitive(self):
        self.assertFalse(check_activity("x", "legitimate_interest", sensitive=True)[0])


class TestPseudonymize(unittest.TestCase):
    def test_same_cpf_same_pseudonym(self):
        self.assertEqual(pseudonymize_cpf("123.456.789-09"), pseudonymize_cpf("12345678909"))

    def test_mask(self):
        self.assertEqual(mask_cpf("123.456.789-09"), "***.456.789-**")

    def test_age_range(self):
        self.assertEqual(anonymize_age(1998), "20-29")


class TestSubjectRequests(unittest.TestCase):
    def test_deadline_is_15_days(self):
        r = SubjectRequest("Ana", "access", date(2026, 10, 1))
        self.assertEqual(r.deadline(), date(2026, 10, 16))

    def test_late(self):
        r = SubjectRequest("Ana", "access", date(2026, 9, 1))
        self.assertTrue(r.is_late(date(2026, 10, 7)))

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            SubjectRequest("Ana", "free_pizza", date(2026, 10, 1))


if __name__ == "__main__":
    unittest.main()
