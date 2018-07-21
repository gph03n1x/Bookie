from django.views.generic import DetailView, FormView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from books.models import Book, UserOrder, BookReview
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def split_into_rows(A, n=4):
    return [A[i:i + n] for i in range(0, len(A), n)]


class BooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'index.html'
    queryset = split_into_rows(Book.objects.all())


class MyBooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'my_books.html'


class CartListView(LoginRequiredMixin, ListView):
    model = UserOrder
    template_name = 'cart.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        # todo get book reviews here too.
        print(context)
        return context
