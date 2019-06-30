from django.urls import path
from app7 import views

urlpatterns = [
    path('', views.usersView,name='users')
    ]


