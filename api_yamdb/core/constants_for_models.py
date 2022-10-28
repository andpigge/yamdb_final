from django.core.validators import MaxValueValidator, MinValueValidator

USER_FIELDS_MAX_LENGTH = {
    'username': 50,
    'role': 10,
    'bio': 200
}

GENERAL_MODEL_FIELDS_MAX_LENGTH = {
    'name': 64,
    'slug': 40
}

TITLE_FIELDS_MAX_LENGTH = {
    'name': 64
}

REVIEW_FIELDS_MAX_LENGTH = {
    'score': {
        'min_value_validator': MinValueValidator(1),
        'max_value_validator': MaxValueValidator(10)
    }
}
