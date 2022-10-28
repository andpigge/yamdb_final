import datetime as dt

from django.core.exceptions import ValidationError


def validate_username(username):
    error_name = 'me'
    if username == error_name:
        raise ValidationError('Указанный username не допустим!')


def validate_year(value):
    year = dt.date.today().year
    if (int(value) > int(year)):
        raise ValidationError('Дата некоректна!')
