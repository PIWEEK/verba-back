from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from quotes.filters import QuoteFilter
from quotes.models import Author, Quote, Tag
from quotes.serializers import AuthorSerializer, QuoteSerializer, TagSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class QuoteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = QuoteFilter
    filter_fields = ('author', 'tags__name')
    ordering = ('?',)

    @list_route()
    def count(self, request):
        return Response(self.filter_queryset(self.get_queryset()).count())


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
