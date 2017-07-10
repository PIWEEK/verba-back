from rest_framework import serializers
from quotes.models import Author, Quote

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    quotes = serializers.HyperlinkedRelatedField(many=True, view_name='quotes-list', read_only=True)
    class Meta:
        model = Author
        fields = ('id', 'name', 'bio', 'birth_date', 'death_date', 'image', 'image_alt', 'wiki_link')


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='author-detail', read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'date', 'source')
