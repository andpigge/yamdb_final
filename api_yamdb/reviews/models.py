from core.constants_for_models import (REVIEW_FIELDS_MAX_LENGTH,
                                       TITLE_FIELDS_MAX_LENGTH,
                                       USER_FIELDS_MAX_LENGTH)
from core.general_models import Date, GeneralModel
from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username, validate_year


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )
    username = models.CharField(
        'Имя пользователя',
        unique=True,
        max_length=USER_FIELDS_MAX_LENGTH.get('username'),
        validators=[validate_username])
    role = models.CharField(
        'Роль пользователя',
        max_length=USER_FIELDS_MAX_LENGTH.get('role'),
        choices=USER_ROLES,
        default='user')
    bio = models.TextField(
        'О себе',
        blank=True,
        max_length=USER_FIELDS_MAX_LENGTH.get('bio'))
    email = models.EmailField(
        'Почта пользователя',
        unique=True
    )

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Genre(GeneralModel):
    class Meta:
        verbose_name = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name[:20]


class Category(GeneralModel):
    class Meta:
        verbose_name = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name[:20]


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        max_length=TITLE_FIELDS_MAX_LENGTH.get('name'))
    year = models.IntegerField(
        'Год',
        validators=[validate_year])
    description = models.TextField(
        'Описание',
        blank=True)
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='title',
        blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категории',
        related_name='title',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Произведение'
        ordering = ('name',)

    def __str__(self):
        return self.name[:20]


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        verbose_name='Произведении'
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE,
        verbose_name='Жанр'
    )

    class Meta:
        db_table = 'reviews_genre_title'
        verbose_name = 'Произведение и жанры'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(Date):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True)
    text = models.TextField('Текст отзыва')
    author = models.ForeignKey(
        CustomUser,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews')
    score = models.PositiveSmallIntegerField(
        'Рейтинг',
        validators=[
            REVIEW_FIELDS_MAX_LENGTH.get('score').get('min_value_validator'),
            REVIEW_FIELDS_MAX_LENGTH.get('score').get('max_value_validator')
        ])

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

        constraints = [
            models.UniqueConstraint(
                name='unique_review',
                fields=['author', 'title']
            )
        ]

    def __str__(self):
        return self.title[:20]


class Comment(Date):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='comments',
        null=True, )
    review = models.ForeignKey(
        Review,
        related_name='comments',
        verbose_name='Отзыв',
        on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(
        CustomUser,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:20]
