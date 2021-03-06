from rest_framework import serializers
from quotes.models import Author, Quote, Tag
from verba import settings


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'url', 'name', 'bio', 'birth_date', 'death_date', 'image', 'image_alt', 'wiki_link')


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    related_quotes = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = ('id', 'url', 'text', 'author', 'date', 'source', 'tags', 'related_quotes')

    def get_related_quotes(self, obj):
        related_quotes = []
        for quote in Quote.objects.all().order_by('?').exclude(id=obj.id)[:3]:
            related_quotes.append({'text': quote.text, 'author_name': quote.author.name, 'url': '{}/api/quotes/{}'.format(settings.BASE_URL, quote.id)})

        return related_quotes
