from django.urls import path
from app6 import views

urlpatterns = [
    path('',views.user_list,name='userlist')

    ]

