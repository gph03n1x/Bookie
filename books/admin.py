from django.contrib import admin
from .models import Book, BookReview


class BookAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'author', 'issued_date', 'description', 'hidden', 'price', 'ISBN', 'pages', 'cover_image']

class BookReviewAdmin(admin.ModelAdmin):
    list_display =  ['user', 'book', 'would_recommend', 'comment']

admin.site.register(Book, BookAdmin)
admin.site.register(BookReview, BookReviewAdmin)
