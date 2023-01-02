from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(LoginRequiredMixin,generic.ListView,generic.FormView):
    queryset = Room.objects.all()
    template_name = 'index.html'
    form_class = RoomForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def form_valid(self,form):
        form.save()
        messages.success(self.request,"room hs been created")
        return super().form_valid(form)


@login_required
def room(request,room_name):
    chat_room = Room.objects.all()
    room = Room.objects.get(slug=room_name)
    room_message = Message.objects.filter(room=room).order_by('timestamp')
    return render(request,'room.html',{'room_name':room_name,'room_message':room_message,'room':room,'chat_room':chat_room})


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
            return redirect('index')    

    return render(request,'registration/signup.html',{'form':form})
