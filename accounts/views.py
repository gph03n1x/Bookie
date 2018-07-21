from django.views.generic import DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from books.models import Book
from django.shortcuts import render, redirect, get_object_or_404

# I've already loaded the necessary classes for my suggestions
# todo: replace this method with a FormView inheriting class-based view
def signup(request):
    """
    Simple signup method validates the data posted, creates an account then authenticates the user.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



class ProfileDetailView(LoginRequiredMixin, DetailView):

    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        if not self.kwargs.get('pk'):
            user = User.objects.get(pk=self.request.user.id)
        else:
            user = User.objects.get(pk=self.kwargs.get('pk'))
        # context['events'] = Event.objects.filter(organiser=user)
        return context

    def get_object(self, *args, **kwargs):
        if not self.kwargs.get('pk'):
            return get_object_or_404(User, pk=self.request.user.id)
        return super(ProfileDetailView, self).get_object(*args, **kwargs)