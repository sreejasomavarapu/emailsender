from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import PlanUser
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model= User
        fields=['username', 'email', 'password1','password2']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

class PlanBookForm(forms.ModelForm):
    class Meta:
        model=PlanUser
        fields=['plan']