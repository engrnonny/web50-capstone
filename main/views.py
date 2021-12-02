
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


# Homepage
# Homepage
# Homepage
def index(request):
    return render(request, "main/index.html")


# About Page
# About Page
# About Page
def about(request):
    return render(request, "main/about.html")


# User Login Page
# User Login Page
# User Login Page
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


# User Logout Page
# User Logout Page
# User Logout Page
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# User Registration Page
# User Registration Page
# User Registration Page
def register(request):
    if request.user.is_authenticated:
        messages.info(request, "Already logged in")
        return redirect("user-profile", slug=request.user.username)

    else:
        if request.method == "POST":
            
            if not request.POST["reg-firstname"]:
                messages.info(request, "Please enter your First Name")
                return redirect("register")

            if not request.POST["reg-lastname"]:
                messages.info(request, "Please enter your Last Name")
                return redirect("register")

            if not request.POST["reg-username"]:
                messages.info(request, "Please enter your Username")
                return redirect("register")

            elif User.objects.filter(username=request.POST["reg-username"]).exists():
                messages.info(request, "Username already exists")
                return redirect("register")

            if not request.POST["reg-phone"]:                
                messages.info(request, "Please enter your Phone Number")
                return redirect("register")

            elif User.objects.filter(phone=request.POST["reg-phone"]).exists():
                messages.info(request, "Phone number already exists")
                return redirect("register")

            if not request.POST["reg-email"]:
                messages.info(request, "Please enter your Email Address")
                return redirect("register")
                
            elif User.objects.filter(email=request.POST["reg-email"]).exists():
                    messages.info(request, "Email address already exists")
                    return redirect("register")

            if not request.POST["reg-password"]:
                messages.info(request, "Please enter your Password")
                return redirect("register")

            else:
                if len(request.POST["reg-password"] ) < 8:
                    messages.info(request, "Password is too short")
                    return redirect("register")
                    
                elif request.POST["reg-password"] != request.POST["reg-password-confirm"]:
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
                        user.phone = phone
                        user.save()

                        if request.POST["reg-gender"]:
                            gender = request.POST["reg-gender"]
                            if gender == "Male" or gender == "Female":
                                user.gender = gender
                                user.save()
                            else: 
                                messages.info(request, "Please select Male or Female in the Gender field")
                                return redirect("register")

                        if request.POST["reg-birthday"]:
                            birthday = request.POST["reg-birthday"]
                            user.birthday = birthday
                            user.save()

                        if request.POST["reg-country"]:
                            country = request.POST["reg-country"]
                            user.country = country
                            user.save()

                        if request.POST["reg-state"]:
                            state = request.POST["reg-state"]
                            user.state = state
                            user.save()

                        if request.POST["reg-lga"]:
                            lga = request.POST["reg-lga"]
                            user.lga = lga
                            user.save()

                        if request.POST["reg-city"]:
                            city = request.POST["reg-city"]
                            user.city = city
                            user.save()

                        if request.POST["reg-address"]:
                            address = request.POST["reg-address"]
                            user.address = address
                            user.save()

                        if request.POST["reg-occupation"]:
                            occupation = request.POST["reg-occupation"]
                            user.occupation = occupation
                            user.save()

                        if request.POST["reg-linkedin"]:
                            linkedin = request.POST["reg-linkedin"]
                            user.linkedin = linkedin
                            user.save()

                        if request.POST["reg-bio"]:
                            bio = request.POST["reg-bio"]
                            user.bio = bio
                            user.save()

                        if "reg-profile-pic" in request.FILES:
                            user.profile_pic = request.FILES["reg-profile-pic"]
                            user.save()


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
        context = {
            'user': user            
        }
        return render(request, "main/user-profile.html", context)
            
    except ObjectDoesNotExist:
        messages.info(request, f"{slug} does not exist")
        return redirect("index")


# Payment Page
# Payment Page
# Payment Page
@login_required
def payment(request):
    return render(request, "main/payment.html")


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
def new_cause(request):
    if request.user.is_authenticated:
        if request.user.monthly_payment == False:
            messages.info(request, "You have not made your monthly donation. Please do so to create a Cause")
            return redirect("payment")
        else:
            if request.method == "POST":
                if request.POST["cause-name"]:
                    if Cause.objects.filter(name=request.POST["cause-name"]).exists():
                        
                        # Use JavaScript here later!!!
                        messages.info(request, "Cause name already exists")
                        return redirect("new-cause")
                    else:
                        name = request.POST["cause-name"]
                        if len(name) <= 128:
                            # Use JavaScript here later!!!
                            messages.info(request, "Name too long")
                            return redirect("new-cause")
                        if request.POST["cause-brief-description"]:
                            cause_brief_description = request.POST["cause-brief-description"]
                        else:
                            messages.info(request, "You must provide a brief description for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-country"]:
                            cause_country = request.POST["cause-country"]
                        else:
                            messages.info(request, "You must provide a country for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-state"]:
                            cause_state = request.POST["cause-state"]
                        else:
                            messages.info(request, "You must provide a state for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-city"]:
                            cause_city = request.POST["cause-city"]
                        else:
                            messages.info(request, "You must provide a city for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-address"]:
                            cause_address = request.POST["cause-address"]
                        if request.POST["cause-duration"]:
                            cause_duration = request.POST["cause-duration"]
                        else:
                            messages.info(request, "You must provide a duration for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-cost"]:
                            cause_cost = request.POST["cause-cost"]
                        else:
                            messages.info(request, "You must provide a cost for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-detail-description"]:
                            cause_detail_description = request.POST["cause-detail-description"]
                        else:
                            messages.info(request, "You must provide a detail description for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-cost-breakdown"]:
                            cause_cost_breakdown = request.POST["cause-cost-breakdown"]
                        else:
                            messages.info(request, "You must provide a cost breakdown for the cause")
                            return redirect("new-cause")
                        if request.POST["cause-expiry"]:
                            cause_expiry = request.POST["cause-expiry"]
                        if request.POST["cause-city"]:
                            cause_city = request.POST["cause-city"]
                        else:
                            messages.info(request, "You must provide a city for the cause")
                            return redirect("new-cause")

                else:
                    # Use JavaScript here later!!!
                    messages.info(request, "Please enter Cause name")
                    return redirect("new-cause")

                    
            else:
                return render(request, "main/new-cause.html")
        
    else:
        messages.info(request, "You must be logged in to create a Cause.")
        return redirect("login")


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
        if "test" in request.FILES:
            test = Test(pic=request.FILES['test'])
            test.save()
            messages.info(request, "Yes")
            return redirect("test")

        else:
            messages.info(request, "No")
            return redirect("test")
        
    else:
        test = Test.objects.all()[1]
        context = {
            'test': test
        }
        return render(request, "main/test.html", context)

