from django_filters import Filter, FilterSet
from quotes.models import Quote


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

    class Meta:
        model = Quote
        fields = ('tags',)

