from django.core.exceptions import ValidationError
INVALID_PHONE_MESSAGE = "Phone number must start with 0 or +"

def validate_phone(value):
    if value is None:
        raise ValidationError("Phone number cannot be empty")

    if not value.startswith("0") and not value.startswith("+"):
        raise ValidationError(INVALID_PHONE_MESSAGE)

