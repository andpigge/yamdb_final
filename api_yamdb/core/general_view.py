from api.mixins import ReadListCreateDestroyMixin
from api.permissions import IsAdminOrReadOnly
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination


class GeneralView(ReadListCreateDestroyMixin):
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    lookup_field = 'slug'

    class Meta:
        abstract = True
