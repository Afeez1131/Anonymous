from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, ProfileForm, MessageForm, PasswordChange    
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):

    return render(request, 'website/index.html', {})

@login_required
def user_home(request):
#https or http= {{request.scheme}}://
# host_name: localhost = {{request.META.HTTP_HOST}}
# message_url + arguments needed = {% url 'message' request.user %}
    return render(request, 'website/user_home.html', {})


def login_user(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
        else:
            messages.warning(request, 'Incorrect Username and / or Password')
    # else:
    #     form = LoginForm()
    return render(request, 'website/login.html', {'form': form,})

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'website/logout_success.html', {})

def register_user(request):
    new_user = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            new_user = form.save(commit=False)
            new_user.set_password(password)
            new_user.save()
            return render(request, 'website/register_success.html', {'new_user': new_user})
    else:
        form = RegisterForm()
    return render(request, 'website/register.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChange(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return render(request, 'website/password_change_success.html', {})
        else:
            
            messages.warning(request, 'Error in the information provided')
    
    else:
        form = PasswordChange(user=request.user)
    return render(request, 'website/password_change.html', {'form': form,})

@login_required
def edit_profile(request):
    if request.method== 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            messages.warning(request, 'Error occured')
    else:
        form = ProfileForm(instance=request.user)
    return render(request,'website/edit_profile.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'website/profile.html', {'user': user})

def user_message(request, user):
    user_name = get_object_or_404(User, username=user)
    user_messages = Message.objects.filter(user=user_name)
    new_message = None
    if request.method == 'POST':
        name = request.POST['username']
        message = request.POST['message']
        new_message = Message.objects.create(user=user_name, name=name, message=message)
        new_message.save()


    return render(request, 'website/message.html', {'user_messages': user_messages,
                                                    'user_name': user_name,})
@login_required                                                    
def delete_message(request, id):    
    message_del = get_object_or_404(Message, id=id)
    message_user = message_del.user
    message_del.delete()
    

    return redirect('message', user=message_user)

@login_required
def spam_message(request, id):
    message_spam = get_object_or_404(Message, id=id)
    message_user = message_spam.user
    message_spam.message = 'Offensive Message.'
    message_spam.save()

    return redirect('message', user=message_user)
