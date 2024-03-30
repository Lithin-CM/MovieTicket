from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    # Example:
    path('signup/', views.signUp, name='signup'),
    path('signin/', views.signIn, name='signin'),
]