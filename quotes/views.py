from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from quotes.models import Author, Quote
from quotes.serializers import AuthorSerializer, QuoteSerializer

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
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('author',)