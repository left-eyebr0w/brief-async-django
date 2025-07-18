from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

# Utiliser un middleware pour la redirection
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "chat/index.html")

# Utiliser un middleware pour la redirection
def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "chat/room.html", {"room_name": room_name})

def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    return LoginView.as_view(template_name="chat/login.html")

# Utiliser un middleware pour la redirection
def logout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect("login")