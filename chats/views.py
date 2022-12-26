from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required
def room(request):
    return render(request,'room.html')


def signUp(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)     
            messages.success(request,"Your account has been created successfully")  
            return redirect('chat-room')    

    return render(request,'registration/signup.html',{'form':form})
