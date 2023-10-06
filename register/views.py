# register/views.py
from .forms import RegistrationForm
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse("Password does not match")
        else:
            myuser = User.objects.create_user(nid, email, pass1)
            myuser.save()
            return redirect('login')

    return render(request, 'register/register_page.html', {'form': RegistrationForm()})

# def register(request):
#     return render(request, 'register/register_page.html', {'form': RegistrationForm()})

# def register_user(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or login page
#             return redirect('user_login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register/register_page.html', {'form': form})


# def login(request):
#     return render(request, 'login/login_page.html')



# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.urls import reverse
# from .forms import register_form
# from django.contrib.auth import authenticate
# from .models import Get_Details


# # Create your views here.


# def register(request):
#     return render(request, "register/register_page.html",{
#         "form": register_form()
#     })

# def login(request):
#     return render(request, "login/login_page.html")


# def register_user(request):
#     context = {}
#     if request.method == "POST":
#         form = register_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("login"))
#     # else:
#     #     return HttpResponse("Invalid request method")
#     context["form"] = form
#     return render(request, "register/register_page.html", context)