
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import ChildInfo
from .forms import ChildInfoForm
from datetime import datetime

# from django.db import models


# Create your views here.

# @login_required(login_url='login')
# def dashboard(request):
#     return render(request, 'dashboard/dashboard_page.html')

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    children = ChildInfo.objects.filter(parent_nid=user)

    if request.method == 'POST':
        form = ChildInfoForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent_nid = user
            current_year = datetime.now().year
            child.age = current_year - child.birth_year
            child.save()
            # Redirect to the dashboard after adding a child
            return redirect('dashboard')
    else:
        form = ChildInfoForm()

    context = {
        'user': user,
        'children': children,
        'form': form,
    }
    return render(request, 'dashboard/dashboard_page.html', context)



def LogoutPage(request):
    logout(request)
    return redirect('home')


# @login_required(login_url='login')
def update_child(request, child_id):
    child = get_object_or_404(ChildInfo, id=child_id)
    if request.method == 'POST':
        form = ChildInfoForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the child list page
    else:
        form = ChildInfoForm(instance=child)
    return render(request, 'dashboard/update_child.html', {'form': form, 'child': child})