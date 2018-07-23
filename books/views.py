from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from books.models import Book, UserOrder, BookReview
from books.forms import ReviewForm
from django.shortcuts import redirect


def split_into_rows(A, n=4):
    return [A[i:i + n] for i in range(0, len(A), n)]


class BooksListView(ListView):
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
        # books = [item.book for item in cart_items]
        return cart_items


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = BookReview.objects.filter(book=context['book'])
        context['user_id'] = self.request.user.id
        return context


@login_required
def add_book_to_cart(request, pk):
    if request.method == 'POST':
        user_order = UserOrder(user=request.user, payed_order=False, book=Book.objects.get(pk=pk))
        user_order.save()
    return redirect('cart')


@login_required
def remove_book_from_cart(request, pk):
    if request.method == 'POST':
        order = UserOrder.objects.get(pk=pk)
        if order.user == request.user:
            order.delete()

        return redirect('cart')


@login_required
def checkout_cart(request):
    if request.method == 'POST':
        user_order = UserOrder.objects.filter(user=request.user, payed_order=False)
        user_order.update(payed_order=True)
    return redirect('my')


@login_required
def create_comment(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.book = Book.objects.get(pk=pk)
            instance.save()

        return redirect('book_detail', pk=pk)


@login_required
def delete_comment(request, pk):
    if request.method == 'POST':
        review = BookReview.objects.get(pk=pk)
        book_pk = review.book.pk
        if review.user == request.user:
            review.delete()

        return redirect('book_detail', pk=book_pk)
