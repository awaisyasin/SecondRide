from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .form import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
import uuid
from .models import CustomUser


# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save()

            current_site = get_current_site(request)
            verification_link = f"http://{current_site}/accounts/verify-email/{user.email_verification_token}/"
            subject = "Email Verification"
            message = f"Click the link below to verify your email: {verification_link}"
            send_mail(subject, message, from_email='info@secondride.com', recipient_list=[user.email])
            return redirect("Accounts:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "Accounts/register.html", {"form": form})


def VerifyEmail(request, token):
    user = CustomUser.objects.get(email_verification_token=token)
    if user:
        user.is_email_verified = True
        user.email_verification_token = None
        user.save()
        return redirect('Accounts:login')
    else:
        return HttpResponse("Verification link is Invalid")


def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get("username")
            # password = form.cleaned_data.get("password")
            user = form.get_user()
            if user.is_email_verified:
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
                login(request, user)
                return redirect("Ads:home")
            else:
                messages.error(request, "Please verify your email!")
                return redirect("Accounts:login")
    else:
        form = AuthenticationForm()
    return render(request, "Accounts/login.html", {"form": form})


def LogoutView(request):
    logout(request)
    return redirect("Ads:home")


def DeleteView(request):
    request.user.delete()
    messages.success(request, 'Your account has been deleted Successfully!')
    return redirect("Accounts:register")