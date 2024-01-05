from unittest import TestCase

from django.core.exceptions import ValidationError

from lost_and_found.objects_posts.validators import validate_phone, INVALID_PHONE_MESSAGE


class ValidatePhoneTests(TestCase):
    def test_when_phone_is_valid_start_with_plus_expect_nothing(self):
        phone = '+3598962600'
        validate_phone(phone)
    def test_when_phone_is_valid_start_with_zero_expect_nothing(self):
        phone = '03598962600'
        validate_phone(phone)
    def test_when_phone__when_not_start_with_plus_or_zero_raises(self):
        phone = '3598962600'
        with self.assertRaises(ValidationError) as ve:
            validate_phone(phone)
        self.assertEqual(INVALID_PHONE_MESSAGE,
                         ve.exception.message)
        self.assertIsNotNone(ve.exception)

