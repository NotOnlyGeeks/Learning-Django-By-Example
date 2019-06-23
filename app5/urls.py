from django.urls import path
from app5 import views

urlpatterns = [
    path('',views.index,name='index')
    ]

