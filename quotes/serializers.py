from rest_framework import serializers
from quotes.models import Author, Quote, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    quotes = serializers.HyperlinkedRelatedField(many=True, view_name='quote-detail', read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'bio', 'birth_date', 'death_date', 'image', 'image_alt', 'wiki_link', 'quotes')


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)

    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'date', 'source', 'tags')