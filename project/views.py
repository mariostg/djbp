from django.shortcuts import render
from project import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    """
    Renders the index page of the project.

    Args:
        request (HttpRequest): The HTTP request object sent by the client.

    Returns:
        HttpResponse: Renders and returns the 'project/index.html' template.
    """
    return render(request, "project/index.html")


def user_login(request):
    """
    Handles user authentication and login process.

    This view function processes both GET and POST requests for user login.
    For POST requests, it authenticates user credentials and manages login sessions.
    For GET requests, it displays the login form.

    Args:
        request (HttpRequest): The HTTP request object containing user data.

    Returns:
        HttpResponse: Renders login page for GET requests or failed authentication.
        HttpResponseRedirect: Redirects to next URL or site-admin upon successful login.

    Raises:
        None explicitly, handles ProjectUser.DoesNotExist internally.

    Notes:
        - Username is converted to lowercase before processing
        - Authentication errors are communicated via Django messages framework
        - Supports redirect to 'next' URL parameter if provided
    """
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
    """Logs out the authenticated user and redirects to login page.

    Args:
        request: HTTP request object containing user session information.

    Returns:
        HttpResponseRedirect: Redirects user to the login page after logout.

    Raises:
        None.
    """
    logout(request)
    return redirect("login")


# @login_required
def siteadmin(request):
    """
    Renders the admin template for the project site.

    Args:
        request: HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: Rendered admin.html template response.
    """
    return render(request, "project/admin.html")
