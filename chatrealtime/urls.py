"""chatrealtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chats import views
from django.contrib.auth.views import PasswordResetView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('chats.urls')),
    path('accounts/password_reset',PasswordResetView.as_view(template_name='registration/password_reset_email.html',html_email_template_name='registration/html_password_reset_email.html'),name='password_reset'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',views.signUp,name='signup'),
]
