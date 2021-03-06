
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db import Error, IntegrityError
from django.db.models import Q
from django.db.utils import load_backend
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
import json

#  Important Variables
month = datetime.datetime.now().month
year = datetime.datetime.now().year

# Homepage
# Homepage
# Homepage
def index(request):
    filtered_causes = Cause.objects.filter(status="Approved").order_by("-votes")[:3]
    causes = []
    
    for cause in filtered_causes:
        try:
            profile_pic = Cause_file.objects.get(cause=cause, file_purpose="Profile Picture")
            new_object = {
                'cause': cause,
                'profile_pic': profile_pic
            }
            causes.append(new_object)
        except Error:
            pass
            
        try: 
            monthly_info = Info.objects.get(month=month, year=year)
        except Error:
            if datetime.datetime.now().day == 1:
                monthly_info = Info(month=month, year=year)
                monthly_info.save()
            else:
                messages.info(request, "Info Object could not be created. Please contact the admin with this message.")
                return redirect("contact")

    context = {
        'causes': causes,
        'monthly_info': monthly_info
    }
    return render(request, "main/index.html", context)


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
            try:
                user_id = User.objects.filter(
                    Q(username=login_user_id) |
                    Q(email=login_user_id)
                )[0]
                user = authenticate(request, username=user_id.username, password=password)

                if user is not None:
                    auth_login(request, user)
                    return redirect("user-profile", slug=user_id.username )
                else:
                    messages.info(request, "Login unsuccessful. Incorrect username/email or password")
                    return redirect("login")
            except IndexError:
                messages.info(request, "Incorrect information")
                return redirect("login")
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
            
            else: 
                test_phone = request.POST["reg-phone"]

                if not int(test_phone):
                    messages.info(request, "Please enter your phone number in digits only")
                    return redirect("register")

                if len(test_phone) < 11 or len(test_phone) > 11:
                    messages.info(request, "Please enter the 11 digits of your phone number")
                    return redirect("register")
                
                if int(test_phone) < 0:
                    messages.info(request, "Please enter positive 11 digits of your phone number")
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
                if len(request.POST["reg-password"]) < 8:
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
def user_profile(request, slug):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=slug)
            context = {
                'user': user            
            }
            return render(request, "main/user-profile.html", context)
                
        except ObjectDoesNotExist:
            messages.info(request, f"{slug} does not exist")
            return redirect("index")
    else:
        messages.info(request, "Please login to view profile")
        return redirect("login")


# User Profile Edit
# User Profile Edit
# User Profile Edit
@login_required
def user_profile_edit(request):
    if request.method == "POST":
        
        if request.POST["edit-firstname"]:
            request.user.first_name = request.POST["edit-firstname"]
            request.user.save()
            

        if request.POST["edit-lastname"]:
            request.user.last_name = request.POST["edit-lastname"]
            request.user.save()

        if request.POST["edit-username"]:

            if User.objects.filter(username=request.POST["edit-username"]).exists():
                messages.info(request, "Username already exists")
                return redirect("user-profile-edit")
            
            else:
                request.user.username = request.POST["edit-username"]
                request.user.save()

        if request.POST["edit-phone"]: 

            if User.objects.filter(phone=request.POST["edit-phone"]).exists():
                messages.info(request, "Phone number already exists")
                return redirect("user-profile-edit")
            
            else: 
                test_phone = request.POST["edit-phone"]

                if not int(test_phone):
                    messages.info(request, "Please enter your phone number in digits only")
                    return redirect("user-profile-edit")

                elif len(test_phone) < 11 or len(test_phone) > 11:
                    messages.info(request, "Please enter the 11 digits of your phone number")
                    return redirect("user-profile-edit")
                
                elif int(test_phone) < 0:
                    messages.info(request, "Please enter positive 11 digits of your phone number")
                    return redirect("user-profile-edit")

                else:
                    request.user.phone = request.POST["edit-phone"]
                    request.user.save()

        if request.POST["edit-email"]:
            
            if User.objects.filter(email=request.POST["edit-email"]).exists():
                messages.info(request, "Email address already exists")
                return redirect("user-profile-edit")
            
            else:
                request.user.email = request.POST["edit-email"]
                request.user.save()

        if request.POST["edit-password"]:

            if len(request.POST["edit-password"] ) < 8:
                messages.info(request, "Password is too short")
                return redirect("user-profile-edit")
                
            if request.POST["edit-password-confirm"]:

                if request.POST["edit-password"] != request.POST["edit-password-confirm"]:
                    messages.info(request, "Passwords do not match")
                    return redirect("user-profile-edit")
                
                else:
                    request.user.set_password(request.POST["edit-password"])
                    request.user.save()
            
            else:
                messages.info(request, "Please enter your password also in Retype Password field")
                return redirect("user-profile-edit")

        if request.POST["edit-gender"]:
            gender = request.POST["edit-gender"]
            if gender == "Male" or gender == "Female":
                request.user.gender = gender
                request.user.save()
            else: 
                messages.info(request, "Please select Male or Female in the Gender field")
                return redirect("user-profile-edit")

        if request.POST["edit-birthday"]:
            request.user.birthday = request.POST["edit-birthday"]
            request.user.save()

        if request.POST["edit-country"]:
            request.user.country = request.POST["edit-country"]
            request.user.save()

        if request.POST["edit-state"]:
            request.user.state = request.POST["edit-state"]
            request.user.save()

        if request.POST["edit-lga"]:
            request.user.lga = request.POST["edit-lga"]
            request.user.save()

        if request.POST["edit-city"]:
            request.user.city = request.POST["edit-city"]
            request.user.save()

        if request.POST["edit-address"]:
            request.user.address = request.POST["edit-address"]
            request.user.save()

        if request.POST["edit-occupation"]:
            request.user.occupation = request.POST["edit-occupation"]
            request.user.save()

        if request.POST["edit-linkedin"]:
            request.user.linkedin = request.POST["edit-linkedin"]
            request.user.save()

        if request.POST["edit-bio"]:
            request.user.bio = request.POST["edit-bio"]
            request.user.save()

        if "edit-profile-pic" in request.FILES:
            request.user.profile_pic = request.FILES["edit-profile-pic"]
            request.user.save()

        messages.info(request, "Your profile was successfully updated.")
        return redirect("user-profile", slug=request.user.username)
    
    else:
        return render(request, "main/user-profile-edit.html")


# Donation Page
# Donation Page
# Donation Page
@login_required
def donate(request):
    return render(request, "main/donate.html")


# Payment Portal
# Payment Portal
# Payment Portal
@login_required
def pay(request):

    user = request.user
    user.total_contribution += 100
    user.save()
    user.monthly_donation = True
    user.save()

    try: 
        monthly_info = Info.objects.get(month=month, year=year)
        monthly_info.total_amount += 100
        monthly_info.save()
        messages.info(request, "Payment successful. Please vote for a Cause")
        return redirect("causes")

    except Error:

        if datetime.datetime.now().day == 1:
            monthly_info = Info(month=month, year=year)
            monthly_info.save()
            monthly_info.total_amount += 100
            monthly_info.save()
            messages.info(request, "Payment successful. Please vote for a Cause")
            return redirect("causes")

        else:
            messages.info(request, "Info Object could not be created. Please contact the admin with this message.")
            return redirect("contact")


# Vote of Unvote
# Vote of Unvote
# Vote of Unvote
@csrf_exempt
@login_required
def vote(request, cause_id):
    if request.method == "PUT":
        try:
            cause = Cause.objects.get(id=cause_id)
            voted = User.objects.filter(voters__id=cause.id, id=request.user.id)
            if request.user.monthly_vote == True:
                if voted:
                    cause.voters.remove(request.user)
                    cause.votes -= 1
                    cause.save()
                    request.user.monthly_vote = False
                    request.user.save()
                    return JsonResponse({"success": "Unvoted successfully"}, status=201)

                else:
                    return JsonResponse({"error": "You have already voted on another Cause."}, status=400)

            else:
                cause.voters.add(request.user)
                cause.votes += 1
                cause.save()
                request.user.monthly_vote = True
                request.user.save()
                return JsonResponse({"success": "Voted successfully"}, status=201)

        
        except IntegrityError:
            return JsonResponse({"error": "Cause not found."}, status=400)

    else:
        return JsonResponse({"error": "PUT method required."}, status=400)


# Causes Page
# Causes Page
# Causes Page
def causes(request):
    cause_list = Cause.objects.all().order_by("name")
    causes = []
    
    for cause in cause_list:
        try:
            profile_pic = Cause_file.objects.get(cause=cause, file_purpose="Profile Picture")
            new_object = {
                'cause': cause,
                'profile_pic': profile_pic
            }
            causes.append(new_object)
        except Error:
            pass

    paginator = Paginator(causes, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'causes': causes,
        'page_obj': page_obj
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
        comments = Comment.objects.filter(cause=cause).order_by('-date_added')
        volunteers = User.objects.filter(volunteers__id=cause.id)
        voters = User.objects.filter(voters__id=cause.id)
        context = {
            'backers': backers,
            'cause': cause,
            'cause_files': cause_files,
            'comments': comments,
            'volunteers': volunteers,
            'voters': voters
        }
        return render(request, "main/cause.html", context)
    
    except ObjectDoesNotExist:
        messages.info(request, f"{slug} does not exist as a Cause")
        return redirect("causes")


# New Cause Page
# New Cause Page
# New Cause Page
def new_cause(request):
    cause_categories = [
        'Economic Growth',
        'Education',
        'Environmental Sanitation',
        'Food',
        'Health',
        'Human Rights',
        'Infrastructure',
        'Security',
        'Skill Acquisition'
    ]

    sub_categories = {
        'Economic Growth': [
            'Industry',
            'Innovation and Technology',
            'Job Creation'
        ],

    }

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

    if request.user.is_authenticated:
        if request.user.monthly_donation == False:
            messages.info(request, "You have not made your monthly donation. Please do so to create a Cause")
            return redirect("donate")
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

                if not request.POST["cause-category"]:
                    messages.info(request, "Please choose a category for the Cause")
                    return redirect("new-cause")

                elif request.POST["cause-category"] not in cause_categories:
                    messages.info(request, "Please choose a category for the Cause")
                    return redirect("new-cause")

                if not request.POST["cause-cost"]:
                    messages.info(request, "Please enter the total cost of the Cause (in Naira)")
                    return redirect("new-cause")

                else:
                    try:
                        cost = int(request.POST["cause-cost"])
                        if cost <= 0:
                            messages.info(request, "Please enter the total cost of the Cause in positive numbers greater than 0 only (in Naira)")
                            return redirect("new-cause")

                    except: 
                        messages.info(request, "Please enter the total cost of the Cause in numbers only (in Naira)")
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
                
                if request.POST["cause-expiration"]:
                    try:
                        expiration = int(request.POST["cause-expiration"])
                    except: 
                        messages.info(request, "Please enter the expiration time of the the Cause in numbers only (in days)")
                        return redirect("new-cause")


                if not request.POST["cause-duration"]:
                    messages.info(request, "Please enter the duration the Cause would take to be completed (in days).")
                    return redirect("new-cause")

                else:
                    try:
                        duration = int(request.POST["cause-duration"])
                    except: 
                        messages.info(request, "Please enter the duration the Cause would take to be completed in numbers only (in days)")
                        return redirect("new-cause")
                    
                if not request.POST["cause-detail-description"]:
                    messages.info(request, "Please give detail description of the Cause")
                    return redirect("new-cause")

                if not request.POST["cause-cost-breakdown"]:
                    messages.info(request, "Please give detail breakdown of the cost of the Cause")
                    return redirect("new-cause")

                if "file-upload" not in request.FILES:
                    messages.info(request, "Please upload a file for the Cause")
                    return redirect("new-cause")

                if not request.POST["file-purpose"]:
                    messages.info(request, "Please choose the purpose of the file being uploaded for the Cause")
                    return redirect("new-cause")

                elif request.POST["file-purpose"] not in file_purposes:
                    messages.info(request, "Please choose the purpose of the file being uploaded for the Cause")
                    return redirect("new-cause")

                if not request.POST["file-type"]:
                    messages.info(request, "Please choose the type of the file being uploaded for the Cause")
                    return redirect("new-cause")

                elif request.POST["file-type"] not in file_types:
                    messages.info(request, "Please choose the type of the file being uploaded for the Cause")
                    return redirect("new-cause")

                if not request.POST["file-description"]:
                    messages.info(request, "Please describe the file being uploaded for the cause")
                    return redirect("new-cause")
                                        
                else:
                    name = request.POST["cause-name"]
                    brief_description = request.POST["cause-brief-description"]
                    category = request.POST["cause-category"]
                    country = request.POST["cause-country"]
                    state = request.POST["cause-state"]
                    city = request.POST["cause-city"]
                    address = request.POST["cause-address"]
                    duration = request.POST["cause-duration"]
                    expiration = request.POST["cause-expiration"]
                    detail_description = request.POST["cause-detail-description"]
                    cost_breakdown = request.POST["cause-cost-breakdown"]
                    cause_slug = slugify(name)
                    file_type = request.POST["file-type"]
                    file_purpose = request.POST["file-purpose"]
                    file_description = request.POST["file-description"]
                    file_upload = request.FILES["file-upload"]

                    try:
                        cause = Cause(name=name.title(), category=category, brief_description=brief_description, country=country.title(), state=state.title(), city=city.title(), address=address, duration=duration, cost=cost, detail_description=detail_description, cost_breakdown=cost_breakdown, status="Awaiting Approval", creator=request.user, slug=cause_slug)
                        cause.save()

                        cause_file = Cause_file(cause=cause, file_type=file_type, file_purpose=file_purpose, file_description=file_description, file_upload=file_upload)
                        cause_file.save()

                        if expiration:
                            cause.expiration = expiration
                            cause.save()
                        
                        messages.info(request, "Cause successfully created")

                        return redirect("cause", slug=cause.slug )
                    
                    except Error:
                        messages.info(request, "Something went wrong. Please Try again later or contact the admin")
                        return redirect("contact")

                    
            else:
                context = {
                    'cause_categories': cause_categories,
                    'file_purposes': file_purposes,
                    'file_types': file_types
                }
                return render(request, "main/new-cause.html", context)
        
    else:
        messages.info(request, "You must be logged in to create a Cause.")
        return redirect("login")


# Comment on a Cause
# Comment on a Cause
# Comment on a Cause
@csrf_exempt
@login_required
def comment(request, cause_id):

    if request.method == "POST":

            try:
                cause = Cause.objects.get(id=cause_id)
                data = json.loads(request.body)
                comment = data.get("comment", "")

                if not comment:
                    return JsonResponse({"error": "Please type in a message in the text field."}, status=400)

                else:
                    new_comment = Comment(cause=cause, comment=comment, user=request.user)
                    new_comment.save()
                    return JsonResponse({
                        "success": "Comment posted successfully",
                        "username": request.user.username
                        }, status=201)
            
            except Error:
                return JsonResponse({"error": "Cause not found."}, status=400)

    else:
        return JsonResponse({"error": "POST method required."}, status=400)
    

# Contact Page
# Contact Page
# Contact Page
def contact(request):
    return render(request, "main/contact.html")


def cancel(request):
    return HttpResponseRedirect(request.session['previous'])


# Test Page
# Test Page
# Test Page
def test(request):
    
    return render(request, "main/test.html")

