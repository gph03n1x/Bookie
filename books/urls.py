from django.urls import path
from . import views

urlpatterns = [
    path('book/<pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('my/', views.MyBooksListView.as_view(), name='profile'),
    path('cart/', views.CartListView.as_view(), name='profile'),
    path('', views.BooksListView.as_view(), name='index'),
]
