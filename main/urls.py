
from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("users/p/<slug>/", views.user_profile, name="user-profile"),
    path("users/edit/p/", views.user_profile_edit, name="user-profile-edit"),
    path("causes/", views.causes, name="causes"),
    path("causes/<slug>/", views.cause, name="cause"),
    path("causes/new/", views.new_cause, name="new-cause"),
    path("donate/", views.donate, name="donate"),
    path("donate/pay/", views.pay, name="pay"),
    path("causes/v/<int:cause_id>", views.vote, name="vote"),
    path("causes/c/<int:cause_id>", views.comment, name="comment"),
    path("contact/", views.contact, name="contact"),
    path("cancel/", views.cancel, name="cancel"),
    path("test/", views.test, name="test"),
]