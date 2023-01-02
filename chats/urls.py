from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('chat/<str:room_name>/',views.room,name='chat-room'),
]
