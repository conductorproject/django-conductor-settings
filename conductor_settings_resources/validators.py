import re

from django.core.exceptions import ValidationError


def validate_no_whitespace(value):
    if re.search(r"\s", value) is not None:
        raise ValidationError("white space is not allowed")
