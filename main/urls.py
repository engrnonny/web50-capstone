
from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("users/p/<slug>", views.user_profile, name="user-profile"),
    path("payment", views.payment, name="payment"),
    path("causes", views.causes, name="causes"),
    path("causes/new/", views.new_cause, name="new-cause"),
    path("contact", views.contact, name="contact"),
    path("test", views.test, name="test"),
]