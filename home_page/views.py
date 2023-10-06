from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    return redirect(reverse("home"))


def home(request):
    return render(request, "home_page/home.html")
