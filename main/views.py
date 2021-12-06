
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.core.exceptions import ObjectDoesNotExist
from django.db import Error, IntegrityError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.text import slugify
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
                    messages.info(request, "Login unsuccessful. Incorrect username/email or password")
                    return redirect("login")
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
                        return redirect("contact")

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

# Single Cause Page
# Single Cause Page
# Single Cause Page
def cause(request, slug):

    try:
        cause = Cause.objects.get(slug=slug)
        backers = User.objects.filter(backers__id=cause.id)
        cause_files = Cause_file.objects.filter(cause=cause)
        volunteers = User.objects.filter(volunteers__id=cause.id)
        context = {
            'backers': backers,
            'cause': cause,
            'cause_files': cause_files,
            'volunteers': volunteers
        }

        print(len(cause_files))
        return render(request, "main/cause.html", context)
    
    except ObjectDoesNotExist:
        messages.info(request, f"{slug} does not exist as a Cause")
        return redirect("causes")


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

                if not request.POST["cause-name"]:
                    messages.info(request, "Please enter a Cause Name")
                    return redirect("new-cause")

                elif Cause.objects.filter(name=request.POST["cause-name"]).exists():                    
                    # Use JavaScript here later!!!
                    messages.info(request, "Cause name already exists")
                    return redirect("new-cause")

                elif len(request.POST["cause-name"]) > 128:
                            # Use JavaScript here later!!!
                            messages.info(request, "Cause name too long. Please ensure it is not more than 128 characters.")
                            return redirect("new-cause")

                if not request.POST["cause-brief-description"]:
                    messages.info(request, "Please enter a brief description of the Cause")
                    return redirect("new-cause")

                if not request.POST["cause-country"]:
                    messages.info(request, "Please enter the country the Cause is located in.")
                    return redirect("new-cause")

                if not request.POST["cause-state"]:
                    messages.info(request, "Please enter the state the Cause is located in.")
                    return redirect("new-cause")

                if not request.POST["cause-city"]:
                    messages.info(request, "Please enter the city the Cause is located in.")
                    return redirect("new-cause")

                if not request.POST["cause-duration"]:
                    messages.info(request, "Please enter the duration the Cause would take to be completed (in days).")
                    return redirect("new-cause")

                if not request.POST["cause-cost"]:
                    messages.info(request, "Please enter the total cost of the Cause (in Naira)")
                    return redirect("new-cause")
                    
                if not request.POST["cause-detail-description"]:
                    messages.info(request, "Please give detail description of the Cause")
                    return redirect("new-cause")

                if not request.POST["cause-cost-breakdown"]:
                    messages.info(request, "Please give detail breakdown of the cost of the Cause")
                    return redirect("new-cause")
                                        
                else:
                    name = request.POST["cause-name"]
                    brief_description = request.POST["cause-brief-description"]
                    country = request.POST["cause-country"]
                    state = request.POST["cause-state"]
                    city = request.POST["cause-city"]
                    address = request.POST["cause-address"]
                    duration = request.POST["cause-duration"]
                    cost = request.POST["cause-cost"]
                    detail_description = request.POST["cause-detail-description"]
                    cost_breakdown = request.POST["cause-cost-breakdown"]
                    expiration = request.POST["cause-expiration"]
                    cause_slug = slugify(name)

                    try:
                        cause = Cause(name=name.title(), brief_description=brief_description, country=country.title(), state=state.title(), city=city.title(), address=address, duration=duration, cost=cost, detail_description=detail_description, cost_breakdown=cost_breakdown, expiration=expiration, status="Awaiting approval", creator=request.user, slug=cause_slug)
                        cause.save()

                        return redirect("cause", slug=cause.slug )
                    
                    except Error:
                        messages.info(request, "Something went wrong. Please Try again later or contact the admin")
                        return redirect("contact")

                    
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
    file_purposes = [
        "Investigation Files", 
        "Ongoing Report", 
        "Profile Picture", 
        "Proof of Completion", 
        "Proof of Payment", 
        "Proof of Existence"
        ]

    file_types = [
        "Image",
        "Document",
        "Video"
    ]

    if request.method == "POST":
        if "file-upload" not in request.FILES:
            messages.info(request, "Please upload a file for the Cause")
            return redirect("test")

        if not request.POST["file-purpose"]:
            messages.info(request, "Please choose the purpose of the file being uploaded for the Cause")
            return redirect("test")

        elif request.POST["file-purpose"] not in file_purposes:
            messages.info(request, "Please choose the purpose of the file being uploaded for the Cause")
            return redirect("test")

        if not request.POST["file-type"]:
            messages.info(request, "Please choose the type of the file being uploaded for the Cause")
            return redirect("test")

        elif request.POST["file-type"] not in file_types:
            messages.info(request, "Please choose the type of the file being uploaded for the Cause")
            return redirect("test")

        if not request.POST["file-description"]:
            messages.info(request, "Please describe the file being uploaded for the cause")
            return redirect("test")

        else:
            cause = Cause.objects.get(id=2)
            file_type = request.POST["file-type"]
            file_purpose = request.POST["file-purpose"]
            file_description = request.POST["file-description"]
            file_upload = request.FILES["file-upload"]
            test = Cause_file(cause=cause, file_type=file_type, file_purpose=file_purpose, file_description=file_description, file_upload=file_upload)
            test.save()
            messages.info(request, "File successfully uploaded")
            return redirect("test")

        
    else:
        context = {
            'file_purposes': file_purposes,
            'file_types': file_types
        }
        return render(request, "main/test.html", context)

