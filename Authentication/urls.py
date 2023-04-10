from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in),
    path('signup', views.sign_up, name='signup'),
    path('signin', views.sign_in, name='signin'),
]