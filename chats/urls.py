from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('chat/',views.room,name='chat-room'),
]
