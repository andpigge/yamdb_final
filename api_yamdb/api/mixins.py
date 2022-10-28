from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet


class ReadListCreateDestroyMixin(ListModelMixin, CreateModelMixin,
                                 DestroyModelMixin, GenericViewSet):
    pass
