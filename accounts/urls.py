from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/profile/<pk>', views.ProfileDetailView.as_view(), name='profile'),
    # path('accounts/profile/', views.ProfileDetailView.as_view(), name='profile'),
]
