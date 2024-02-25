from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

@login_required
def special_page(request):
    return render(request, "main/special_page.html")
