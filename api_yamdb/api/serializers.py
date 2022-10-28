import datetime as dt

from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Category, Comment, CustomUser, Genre, Review, Title


class UserSerializer(serializers.ModelSerializer):
    """
    Отдать клиенту поля модели CustomUser.
    Поля role только для чтения.
    """

    class Meta:
        model = CustomUser

        fields = (
            'first_name', 'last_name',
            'bio', 'username',
            'email', 'role'
        )

        read_only_field = ('role',)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class ReviewSerializer(serializers.ModelSerializer):
    """
    Отдать клиенту поля модели Review.
    Пользователь может отправить только один отзыв.
    Поля author только для чтения.
    """

    author = SlugRelatedField(slug_field="username", read_only=True)

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        author = self.context['request'].user
        title_id = self.context['view'].kwargs['title_id']

        if Review.objects.filter(author=author, title_id=title_id).exists():
            raise serializers.ValidationError(
                'Отзыв уже оставлен!'
            )

        return data

    class Meta:
        model = Review

        fields = (
            'id', 'text',
            'author', 'score',
            'pub_date'
        )


class CommentSerializer(serializers.ModelSerializer):
    """
    Отдать клиенту поля модели Review.
    Поля author только для чтения.
    """

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class GenreSerializer(serializers.ModelSerializer):
    """ Отдать клиенту поля модели Genre. """

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    """ Отдать клиенту поля модели Category. """

    class Meta:
        model = Category
        fields = ('name', 'slug')


class TitleListSerializer(serializers.ModelSerializer):
    """
    Используется только для чтения.
    Отдать клиенту поля модели Title.
    Формировать поле rating как среднее значение.
    """

    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = '__all__'

    rating = serializers.SerializerMethodField()

    def get_rating(self, ob):
        return ob.reviews.all().aggregate(Avg('score'))['score__avg']


class TitleSerializer(TitleListSerializer):
    """
    Отдать клиенту поля модели Title.
    Поля rating только для чтения.
    """

    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True,
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )

    def validate_year(self, value):
        year = dt.date.today().year
        if (year >= value > 0):
            return value
        raise serializers.ValidationError(f'Год не должен быть больше'
                                          f'текущего - {year}')

    class Meta:
        model = Title
        fields = (
            'id', 'name',
            'year', 'rating',
            'description',
            'genre', 'category'
        )
        read_only_field = fields
