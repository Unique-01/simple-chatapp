from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=300,required=True)
    first_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=50,required=False)

    def clean(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']

        if User.objects.filter(email=email).exists():
            raise ValidationError("User with that email already exist!")

        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already taken')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


    