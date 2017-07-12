import random
from django.db import connection
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import list_route
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
    filter_backends = (DjangoFilterBackend,)
    filter_class = QuoteFilter
    filter_fields = ('author', 'tags__name')

    def list(self, request, *args, **kwargs):
        seed = request.query_params.get('seed', random.random())
        self.postgres_setseed(seed)
        random_quotes = Quote.objects.all().order_by('?')
        filtered_quotes = self.filter_queryset(random_quotes)

        page = self.paginate_queryset(filtered_quotes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)

            if self.seed_needed(response.data['next']):
                response.data['next'] = ''.join([response.data['next'], '&seed=', str(seed)])

            if self.seed_needed(response.data['previous']):
                response.data['previous'] = ''.join([response.data['previous'], '&seed=', str(seed)])
        else:
            serializer = self.get_serializer(filtered_quotes, many=True)
            response = Response(serializer.data)

        return response

    def postgres_setseed(self, seed):
        cursor = connection.cursor()
        cursor.execute("SELECT setseed(%s);" % seed)
        cursor.close()

    def seed_needed(self, url):
        return url is not None and 'seed' not in url

    @list_route()
    def count(self, request):
        return Response(self.filter_queryset(self.get_queryset()).count())


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
