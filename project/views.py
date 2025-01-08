from django.shortcuts import render
from project import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    return render(request, "project/index.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = models.ProjectUser.objects.get(username=username)
        except models.ProjectUser.DoesNotExist:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET["next"] if "next" in request.GET else "site-admin")
        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, "project/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


# @login_required
def siteadmin(request):
    return render(request, "project/admin.html")
