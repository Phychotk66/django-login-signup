from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.
#signup from django
def sign (request):

    if request.method == "POST":
        em = Signup(request.POST)
        if em.is_valid():
            messages.success(request, 'Acount Created Successfuly')
            em.save()
    else:
        em = Signup()
    return render(request, 'log.html', {'from':em}) 

#login from django
def login_user(request):
    if not request.user.is_authenticated:
     if request.method == 'POST':
        em = AuthenticationForm(request=request, data=request.POST)
        if em.is_valid():
            usname = em.cleaned_data['username']
            upass = em.cleaned_data['password']
            user = authenticate(username=usname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'login sucessfull')
                return HttpResponseRedirect('/profile/')
     else:
       em = AuthenticationForm()
     return render(request, 'login.html', {'from':em})
    else:
        return HttpResponseRedirect('/profile/')

#profile pages
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
             if request.user.is_superuser == True:
                em = EditAdminProfileForm(request.POST, instance=request.user)
                user = User.objects.all()
             else:
                em = EditUserProfileForm(request.POST, instance=request.user)
                user = None
             if em.is_valid():
                 messages.success(request, 'Profile Update Successfuly')
                 em.save()
        else:
            if request.user.is_superuser == True:
                em = EditAdminProfileForm(instance=request.user)
                user = User.objects.all()
            else:
              em = EditUserProfileForm(instance=request.user)
              user = None
        return render(request, 'profile.html', {'name': request.user, 'from':em, 'user': user})
    else:
        return HttpResponseRedirect ('/login/')
    #logout pages
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#ChangePassword
def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            em = PasswordChangeForm(user=request.user, data=request.POST)
            if em.is_valid():
                em.save()
                update_session_auth_hash(request, em.user)
                messages.success(request, 'password change successfuly')
                return HttpResponseRedirect('/profile/')

        else:
            em = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'from':em})
    else:
        return HttpResponseRedirect('/login/')



def userdts(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        em = EditAdminProfileForm(instance=pi)
        return render(request, 'userdetils.html', {'from':em})
    else:
        return HttpResponseRedirect('/login/')