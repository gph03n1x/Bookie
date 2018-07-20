from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'author', 'issued_date', 'description', 'hidden', 'price', 'ISBN', 'pages', 'cover_image']


admin.site.register(Book, BookAdmin)
