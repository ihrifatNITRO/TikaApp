# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import LoginForm
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=nid, password=pass1)
        if user is not None:
            auth_login(request, user)
            # Redirect to the desired page after successful login
            return redirect('dashboard')
        else:
            # Handle invalid login
            error_message = "Invalid NID or password. Please try again."
            return render(request, 'login/login_page.html', {'form': LoginForm(), 'error_message': error_message})
    
    return render(request, 'login/login_page.html', {'form': LoginForm()})

# def login(request):
#     return render(request, 'login/login_page.html', {'form': LoginForm()})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 #login(request, user)
#                 # Redirect to the desired page after successful login
#                 return redirect('home')
#             else:
#                 # Handle invalid login
#                 error_message = "Invalid email or password. Please try again."
#                 return render(request, 'login/login_page.html', {'form': form, 'error_message': error_message})
#     else:
#         form = LoginForm()
#     return render(request, 'login/login_page.html', {'form': form})


# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.urls import reverse
# from .forms import login_form
# from django.contrib.auth import authenticate, login, logout

# # Create your views here.


# def login(request):
#     return render(request, "login/login_page.html",{
#         "form": login_form()
#     })


# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             # Authentication successful, log in the user
#             login(request, user)
#             # Redirect to a success page or perform other actions
#         else:
#             # Authentication failed, display an error message
#             return HttpResponse("Invalid credentials")