from core.general_view import GeneralView
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import Category, CustomUser, Genre, Review, Title

from .filters import TitleFilter
from .permissions import (IsAdmin, IsAdminOrReadOnly,
                          IsAuthorModeratorAdminOrReadOnly)
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleListSerializer, TitleSerializer,
                          TokenSerializer, UserSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def creation_and_confirmation_users(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data.get('email')
    username = serializer.validated_data.get('username')

    CustomUser.objects.create(username=username, email=email)
    user = CustomUser.objects.filter(email=email).first()
    confirmation_code = default_token_generator.make_token(user)

    send_mail(
        'Код подтверждения Yamdb',
        f'Ваш код подтверждения: {confirmation_code}',
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def getting_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    confirmation_code = serializer.validated_data.get(
        'confirmation_code'
    )
    user = get_object_or_404(CustomUser, username=username)

    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)

        return Response(
            {'token': str(token)}, status=status.HTTP_200_OK
        )

    return Response(
        {'confirmation_code': 'Неверный код подтверждения!'},
        status=status.HTTP_400_BAD_REQUEST
    )


class UserViewSet(viewsets.ModelViewSet):
    """ Расширить класс User. """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username',)

    lookup_field = 'username'

    @action(methods=['patch', 'get'],
            permission_classes=[permissions.IsAuthenticated],
            detail=False)
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)

        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role)

        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    CRUD.
    Разрешить запись только авторизированому пользователю.
    """

    serializer_class = ReviewSerializer

    permission_classes = (
        IsAuthorModeratorAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD.
    Разрешить запись только авторизированому пользователю,
    и удаление автору поста.
    """

    serializer_class = CommentSerializer

    permission_classes = (
        IsAuthorModeratorAdminOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly
    )

    def get_queryset(self):
        review = get_object_or_404(
            Review, id=self.kwargs['review_id'],
            title__id=self.kwargs['title_id']
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review, id=self.kwargs['review_id'],
            title__id=self.kwargs['title_id']
        )
        serializer.save(author=self.request.user, review=review)


class TitleViewSet(viewsets.ModelViewSet):
    """
    CRUD. Разрешить запись и удаление только администратору.
    Разрешить собственное разбиение по страницам.
    """

    queryset = Title.objects.all()

    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)

    pagination_class = LimitOffsetPagination
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitleSerializer


class GenreViewSet(GeneralView):
    """
    Create, Read List, Delete.
    Разрешить запись и удаление только администратору.
    Разрешить собственное разбиение по страницам.
    Включить поиск по имени.
    Переопределить ключевое слово для url.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CategoryViewSet(GeneralView):
    """
    Create, Read List, Delete.
    Разрешить запись и удаление только администратору.
    Разрешить собственное разбиение по страницам.
    Включить поиск по имени.
    Переопределить ключевое слово для url.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
