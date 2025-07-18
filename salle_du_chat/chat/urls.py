from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", LoginView.as_view(template_name="chat/login.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path("<str:room_name>/", views.room, name="room"),
]