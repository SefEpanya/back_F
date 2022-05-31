from django.urls import path
from fifi import views
from . import views

urlpatterns = [
    path('', views.fileFinder, name='home'),
    path('signup/', views.registration, name='signup'),
    path('upload/', views.upload, name='upload'),
    path('user/', views.userPage, name='userpage'),

]
