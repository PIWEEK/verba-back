from django_filters import Filter, FilterSet, CharFilter
from django.db.models import Q
from quotes.models import Quote

class AuthorFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        authors = value.split(',')
        q_objects = Q()
        for author in authors:
            q_objects |= Q(author__id=author)
        return qs.filter(q_objects)


class TagsFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        tags = value.split(',')
        for tag in tags:
            qs = qs.filter(tags__name=tag)
        return qs


class QuoteFilter(FilterSet):
    tags = TagsFilter(name='tags')
    author = AuthorFilter(name='author')

    class Meta:
        model = Quote
        fields = ('tags', 'author')

