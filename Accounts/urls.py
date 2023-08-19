from django.urls import path
from . import views

app_name = "Accounts"

urlpatterns = [
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),
    path("delete/", views.DeleteView, name="delete"),
    path("verify-email/<str:token>/", views.VerifyEmail, name="verify_email"),
]