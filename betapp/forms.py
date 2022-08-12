from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password')
class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('email', 'phone_no', 'profile_pic')


class BookingForm(forms.ModelForm):
    class Meta():
        model = BetBooking
        fields = '__all__'
    

    