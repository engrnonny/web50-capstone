
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

def about(request):
    return render(request, "main/about.html")

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "User already logged in")
        return redirect("user-profile", slug=request.user.username)

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
        else:
            return render(request, "main/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.user.is_authenticated:
        messages.info(request, "User already logged in")
        return redirect("user-profile", slug=request.user.username)

    else:
        if request.method == "POST":

            if User.objects.filter(username=request.POST["reg-username"]).exists():
                messages.info(request, "Username already exists")
                return redirect("register")

            else: 
                if User.objects.filter(email=request.POST["reg-email"]).exists():
                    messages.info(request, "Email address already exists")
                    return redirect("register")

                else:
                    if Profile.objects.filter(phone=request.POST["reg-phone"]).exists():
                        messages.info(request, "Phone number already exists")
                        return redirect("register")

                    else:
                        if len(request.POST["reg-password"] ) < 8:
                            messages.info(request, "Password is too short")
                            return redirect("register")
                            
                        else:
                            if request.POST["reg-password"] != request.POST["reg-password-confirm"]:
                                messages.info(request, "Passwords do not match")
                                return redirect("register")

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
                                    print(1)

                                    if request.POST["reg-gender"]:
                                        print(2)
                                        gender = request.POST["reg-gender"]
                                        if gender == "male" or gender == "female":
                                            profile.gender = gender
                                            profile.save()
                                        else: 
                                            messages.info(request, "Your registration was successful. Please login to continue")
                                            return redirect("register")

                                    if request.POST["reg-birthday"]:
                                        print(3)
                                        birthday = request.POST["reg-birthday"]
                                        profile.birthday = birthday
                                        profile.save()

                                    if request.POST["reg-country"]:
                                        print(4)
                                        country = request.POST["reg-country"]
                                        profile.country = country
                                        profile.save()

                                    if request.POST["reg-state"]:
                                        print(5)
                                        state = request.POST["reg-state"]
                                        profile.state = state
                                        profile.save()

                                    if request.POST["reg-lga"]:
                                        print(6)
                                        lga = request.POST["reg-lga"]
                                        profile.lga = lga
                                        profile.save()

                                    if request.POST["reg-city"]:
                                        print(7)
                                        city = request.POST["reg-city"]
                                        profile.city = city
                                        profile.save()

                                    if request.POST["reg-address"]:
                                        print(8)
                                        address = request.POST["reg-address"]
                                        profile.address = address
                                        profile.save()

                                    if request.POST["reg-occupation"]:
                                        print(9)
                                        occupation = request.POST["reg-occupation"]
                                        profile.occupation = occupation
                                        profile.save()

                                    if request.POST["reg-linkedin"]:
                                        print(10)
                                        linkedin = request.POST["reg-linkedin"]
                                        profile.linkedin = linkedin
                                        profile.save()

                                    if request.POST["reg-bio"]:
                                        print(11)
                                        bio = request.POST["reg-bio"]
                                        profile.bio = bio
                                        profile.save()

                                    if request.POST["reg-profile-pic"]:
                                        print(12)
                                        profile_pic = request.POST["reg-profile-pic"]
                                        profile.profile_pic = profile_pic
                                        profile.save()


                                    messages.info(request, "Your registration was successful. Please login to continue")
                                    return redirect("login")

                                except Error:
                                    messages.info(request, "Something went wrong. Please Try again later or contact the admin")
                                    return redirect("index")

        else:
            return render(request, "main/register.html")


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


# Causes Page
# Causes Page
# Causes Page
def causes(request):
    causes = Cause.objects.all()
    context = {
        'causes': causes
    }
    return render(request, "main/causes.html", context)


# New Cause Page
# New Cause Page
# New Cause Page
@login_required
def new_cause(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "main/new-cause.html")



# Contact Page
# Contact Page
# Contact Page
def contact(request):
    return render(request, "main/contact.html")




# Test Page
# Test Page
# Test Page
def test(request):
    if request.method == "POST":
        print(1)
        new_image_name = "Test"
        print(3)
        request.FILES[new_image_name] = request.FILES.get('test')
        print(5)
        user = User.objects.get(username="test1")
        print(6)
        profile = Profile.objects.get(user=user)
        print(7)
        profile.profile_pic = request.FILES[new_image_name]
        print(8)
        profile.save()
        print(9)
        
    else:
        return render(request, "main/test.html")

