from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.
def home_view(request:HttpRequest):
    #returning a template
    return render(request, "main/home.html")

def about_view(request:HttpRequest):
    # returning a template
    return render(request, "main/about.html")

def generate_password(request):
    # logic to generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    return render(request, "main/generate_password.html", {"password": password})