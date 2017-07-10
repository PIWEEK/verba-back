from django.db import models

class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateTimeField(blank=True,null=True)
    death_date = models.DateTimeField(blank=True,null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    wiki_link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('name',)


class Quote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)
    text = models.TextField()
    date = models.DateTimeField(blank=True,null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('author', 'date',)
