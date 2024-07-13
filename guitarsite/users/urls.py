from django.urls import path, re_path


from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('register_done/', views.register_done, name='register_done')
]