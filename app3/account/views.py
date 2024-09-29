from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .forms import CustomUserCreationForm, CustomUserChangeForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # Войти в систему после регистрации
            return redirect('/home/')  # Замените на нужный вам URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/accounts/profile/')  # Замените на нужный URL
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/home/')

@login_required
def profile(request):
    user_profile = (request.user.profile if hasattr(request.user, 'profile') else None)
    return render(request, 'account/profile.html', {'user': request.user, 'profile': user_profile})



# Представление для добавления пользователя
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')  # Замените на нужный вам URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/add_user.html', {'form': form})

# Представление для редактирования пользователя
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')  # Замените на нужный вам URL
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'account/edit_user.html', {'form': form, 'user': user})

# Представление для удаления пользователя
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('/accounts/')  # Замените на нужный вам URL
    return render(request, 'account/delete_user.html', {'user': user})

# Представление для списка пользователей (опционально)
def user_list(request):
    users = User.objects.all()
    return render(request, 'account/user_list.html', {'users': users})