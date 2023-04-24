from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            if username == "aek" and password == "r21":
                request.session["logged_in"] = True
                return redirect("logout")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "shop/login.html", {"form": form})


def logout(request):
    if request.method == "POST":
        request.session.pop("logged_in", None)
        return redirect("login")
    return render(request, "shop/logout.html")
