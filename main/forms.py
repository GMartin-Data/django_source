from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.PasswordInput()
    
    class Meta(UserCreationForm.Meta):
        model = User

