from os import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .models import Member
from .forms import MemberForm, CreateUserForm, LoginForm

# Create your views here.

def index(request):
    return render(request, 'maringo_site/index.html')

def user_register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maringo_site:user_login')
        
    else:
        form = CreateUserForm()

    context = {'form': form}

    return render(request, 'maringo_site/user-register.html', context)



def user_login(request):
    if request.method == 'POST':
        form = LoginForm()
        if form.is_valid():
            form = LoginForm(request, data=request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('maringo_site:dashboard')
        
    else:
        form = LoginForm()

    return render(request, 'maringo_site/user-login.html', {'form': form})




def member_register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = MemberForm()

    return render(request, 'maringo_site/member-register.html', {'form': form})




def members(request):
    form = MemberForm
    names = Member.objects.all()
    ctx = {'names': names,
           'form': form}
    return render(request, 'maringo_site/all-members.html', context=ctx)

     
