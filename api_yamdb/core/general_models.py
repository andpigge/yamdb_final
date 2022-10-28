from django.db import models

from .constants_for_models import GENERAL_MODEL_FIELDS_MAX_LENGTH


class GeneralModel(models.Model):
    name = models.CharField(
        'Жанр',
        max_length=GENERAL_MODEL_FIELDS_MAX_LENGTH.get('name'),
        unique=True)
    slug = models.SlugField(
        'Путь',
        unique=True,
        max_length=GENERAL_MODEL_FIELDS_MAX_LENGTH.get('slug'))

    class Meta:
        abstract = True


class Date(models.Model):
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    edited = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )

    class Meta:
        abstract = True
