from django.urls import path

from . import views

urlpatterns = [
        path('', views.index),
        path('create', views.post_chat),
        path('chats', views.get_chats)
        ]
