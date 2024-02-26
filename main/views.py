from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignupPage(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def eda(request):
    return render(request, 'main/eda.html')

def model(request):
    return render(request, 'main/model.html')

@login_required
def special_page(request):
    return render(request, "main/special_page.html")

@login_required
def predict_page(request):
    return render(request, 'main/predict.html')