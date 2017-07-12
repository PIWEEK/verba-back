from django.contrib import admin
from quotes.models import Author, Quote, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Tag, TagAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Author, AuthorAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('excerpt_text',)
    filter_horizontal = ('tags',)

    def excerpt_text(self, obj):
        return obj.text[:50]
admin.site.register(Quote, QuoteAdmin)
