import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import (Category, Comment, CustomUser, Genre, GenreTitle,
                            Review, Title)


def file_reader(file_name: str):
    path = os.path.join(settings.BASE_DIR, 'static/data/', file_name)
    file = open(path, 'r', encoding='utf-8')
    return csv.reader(file, delimiter=',')


class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_reader = file_reader('category.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj, created = Category.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
        print('category - successfully')

        csv_reader = file_reader('genre.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj, created = Genre.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
        print('genre - successfully')

        csv_reader = file_reader('titles.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj_category = get_object_or_404(Category, id=row[3])
            obj, created = Title.objects.get_or_create(
                id=row[0],
                name=row[1],
                year=row[2],
                category=obj_category
            )
        print('titles - successfully')

        csv_reader = file_reader('genre_title.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj_genre = get_object_or_404(Genre, id=row[2])
            obj_title = get_object_or_404(Title, id=row[1])
            obj, created = GenreTitle.objects.get_or_create(
                id=row[0],
                genre=obj_genre,
                title=obj_title
            )
        print('genre_titles - successfully')

        csv_reader = file_reader('users.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj, created = CustomUser.objects.get_or_create(
                id=row[0],
                username=row[1],
                email=row[2],
                role=row[3],
                bio=row[4],
                first_name=row[5],
                last_name=row[6]
            )
        print('users - successfully')

        csv_reader = file_reader('review.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj_title = get_object_or_404(Title, id=row[1])
            obj_user = get_object_or_404(CustomUser, id=row[3])
            obj, created = Review.objects.get_or_create(
                id=row[0],
                title=obj_title,
                text=row[2],
                author=obj_user,
                score=row[4],
                pub_date=row[5]
            )
        print('review - successfully')

        csv_reader = file_reader('comments.csv')
        next(csv_reader, None)
        for row in csv_reader:
            obj_review = get_object_or_404(Review, id=row[1])
            obj_user = get_object_or_404(CustomUser, id=row[3])
            obj, created = Comment.objects.get_or_create(
                id=row[0],
                review=obj_review,
                text=row[2],
                author=obj_user,
                pub_date=row[4]
            )
        print('comments - successfully')
