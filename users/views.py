from django.shortcuts import render
from users import views

def profile(request, username):
    context = {
        "username" :username,
    }
    return render(request, "users/profile.html",context)

def users(request):
    return render(request, "users/users.html")