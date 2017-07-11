from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Author(models.Model):
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    death_date = models.DateField(blank=True,null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    image_alt = models.CharField(max_length=100, blank=True, null=True)
    wiki_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Quote(models.Model):
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='quotes')
    text = models.TextField()
    date = models.DateField(blank=True,null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('author', 'date',)