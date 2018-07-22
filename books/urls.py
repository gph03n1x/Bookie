from django.urls import path
from . import views

urlpatterns = [
    path('book/<pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/<pk>/cart/', views.add_book_to_cart, name='book_to_cart'),
    path('my/', views.MyBooksListView.as_view(), name='my'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('checkout/', views.checkout_cart, name='checkout'),
    path('', views.BooksListView.as_view(), name='index'),
]
