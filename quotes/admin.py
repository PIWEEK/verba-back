from django.contrib import admin
from quotes.models import Author, Quote

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Author, AuthorAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('excerpt_text',)

    def excerpt_text(self, obj):
        return obj.text[:50]
admin.site.register(Quote, QuoteAdmin)
