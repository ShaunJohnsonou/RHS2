from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Page),
    path('Project_Register', views.Project_Register_Page),
    path('Suggestions', views.Suggestions_Page)

]