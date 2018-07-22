from django.views.generic import DetailView, FormView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.contrib.auth.models import User
from books.models import Book, UserOrder, BookReview
from django.shortcuts import render, redirect, get_object_or_404


def split_into_rows(A, n=4):
    return [A[i:i + n] for i in range(0, len(A), n)]


class BooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'index.html'
    queryset = split_into_rows(Book.objects.all())


class MyBooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'my_books.html'

    def get_queryset(self):
        cart_items = UserOrder.objects.filter(user=self.request.user, payed_order=True)
        books = split_into_rows([item.book for item in cart_items])
        return books


class CartListView(LoginRequiredMixin, ListView):
    model = UserOrder
    template_name = 'cart.html'

    def get_queryset(self):
        cart_items = UserOrder.objects.filter(user=self.request.user, payed_order=False)
        books = [item.book for item in cart_items]
        return books


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_details.html'


@login_required
def add_book_to_cart(request, pk):
    if request.method == 'POST':
        user_order = UserOrder(user=request.user, payed_order=False, book=Book.objects.get(pk=pk))
        user_order.save()
    return redirect('cart')



@login_required
def checkout_cart(request):
    if request.method == 'POST':
        user_order = UserOrder.objects.filter(user=request.user, payed_order=False)
        user_order.update(payed_order=True)
    return redirect('my')


class CreateComment(LoginRequiredMixin, CreateView):
    model = BookReview

class DeleteComment(LoginRequiredMixin, DeleteView):
    model = BookReview

