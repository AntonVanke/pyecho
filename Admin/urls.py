from django.urls import path

from Admin import views

urlpatterns = [
    path("", views.index, name="user_index"),
    path("login.html", views.login, name="user_login"),
    path("register.html", views.register, name="user_register"),
    path("forget.html", views.forget, name="user_forget"),
]