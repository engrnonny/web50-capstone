
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import Error, IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import *

def index(request):
    return render(request, "main/index.html")


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "User already logged in")
        return redirect("index")

    else:
        if request.method == "POST":
            login_user_id = request.POST["login-user-id"]
            password = request.POST["login-password"]
            user_id = User.objects.filter(
                Q(username=login_user_id) |
                Q(email=login_user_id)
            )[0]
            if user_id:
                user = authenticate(request, username=user_id.username, password=password)

                if user is not None:
                    auth_login(request, user)
                    return redirect("user-profile", slug=user_id.username )
                else:
                    messages.info(request, "not logged in")
                    return render(request, "main/index.html")
            else:
                messages.info(request, "Incorrect information")
                return redirect("index")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":

        if User.objects.filter(username=request.POST["reg-username"]).exists():
            messages.info(request, "Username already exists")
            return redirect("index")

        else: 
            if User.objects.filter(email=request.POST["reg-email"]).exists():
                messages.info(request, "Email already exists")
                return redirect("index")

            else:
                if Profile.objects.filter(phone=request.POST["reg-phone"]).exists():
                    messages.info(request, "Phone already exists")
                    return redirect("index")

                else:
                    if len(request.POST["reg-password"] ) < 8:
                        messages.info(request, "Password is too short")
                        return redirect("index")
                        
                    else:
                        if request.POST["reg-password"] != request.POST["reg-password-confirm"]:
                            messages.info(request, "Passwords do not match")
                            return redirect("index")

                        else:
                            first_name = request.POST["reg-firstname"]
                            last_name = request.POST["reg-lastname"]
                            username = request.POST["reg-username"]
                            phone = request.POST["reg-phone"]
                            email = request.POST["reg-email"]
                            password = request.POST["reg-password"]


                            try:
                                user = User.objects.create_user(username, email, password)
                                user.save()
                                user.first_name = first_name
                                user.save()
                                user.last_name = last_name
                                user.save()
                                profile = Profile(user=user, phone=phone)
                                profile.save()
                                messages.info(request, "Your registration was successful. Please login to continue")
                                return redirect("profile")

                            except Error:
                                messages.info(request, "Something went wrong. Please Try again later or contact the admin")
                                return redirect("index")


# User Profile Page
# User Profile Page
# User Profile Page

@login_required
def user_profile(request, slug):
    try:
        user = User.objects.get(username=slug)
        try:
            profile = Profile.objects.get(user=user)
            context = {
                'profile': profile,
                'user': user            
            }
            return render(request, "main/user-profile.html", context)
        
        except ObjectDoesNotExist:
            messages.info(request, f"{slug} has no profile. Please contact the admin if this is your account")
            return redirect("index")
            
    except ObjectDoesNotExist:
        messages.info(request, f"{slug} does not exist")
        return redirect("index")