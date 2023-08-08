from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .form import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Accounts:login")
    else:
        form = CustomUserCreationForm()

    return render(request, "Accounts/register.html", {"form": form})

def LoginView(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Ads:home")
    else:
        form = CustomAuthenticationForm()

    return render(request, "Accounts/login.html", {"form": form})

def LogoutView(request):
    logout(request)
    return redirect("Ads:home")