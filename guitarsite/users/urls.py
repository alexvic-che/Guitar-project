from django.urls import path, re_path
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django import forms

from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('register_done/', views.register_done, name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password_change/', views.UserPasswordChange.as_view(), name='user_password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='users/user_password_change_done.html'), name='user_password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name="users/password_reset_form.html",
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy("users:password_reset_done"),
        ),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="users/password_reset_confirm.html",
        success_url=reverse_lazy("users:password_reset_complete")
        ),
         name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete')
]