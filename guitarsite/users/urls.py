from django.urls import path, re_path
from django.contrib.auth.views import PasswordChangeDoneView

from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('register_done/', views.register_done, name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password_change/', views.UserPasswordChange.as_view(), name='user_password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='users/user_password_change_done.html'), name='user_password_change_done')
]