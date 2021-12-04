
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


# The first entry is what goes into the database, the second is what is displayed.
CATEGORY = (
    ('Infrastructure', 'Infrastructure'),
    ('Health', 'Health')
)

CATEGORY_SLUGS = (
    ('infrastructure', 'infrastructure'),
    ('health', 'health')
)

CAUSE_FILES_USAGE = (
    ('Investigation Files', 'Investigation Files'),
    ('Ongoing Report', 'Ongoing Report'),
    ('Profile Picture', 'Profile Picture'),
    ('Proof of Completion', 'Proof of Completion'),
    ('Proof of Payment', 'Proof of Payment'),
    ('Proof of Existence', 'Proof of Existence')
)

FILE_TYPES = (
    ('Images', 'Images'),
    ('Documents', 'Documents'),
    ('Videos', 'Videos')
)

STATUS = (
    ('Approved', 'Approved'),
    ('Awaiting approval', 'Awaiting approval'),
    ('Completed', 'Completed'),
    ('Ongoing', 'Ongoing'),
    ('Rejected', 'Rejected'),
    ('Suspended', 'Suspended')
)

# Create your models here.

class Cause_categorie(models.Model):
    name = models.CharField(choices=CATEGORY, max_length=64, null=True, blank=True)
    slug = models.SlugField(choices=CATEGORY_SLUGS)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}" 

class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    lga = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    occupation = models.CharField(max_length=64, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'user_followers', blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'user_following', blank=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="main/users/profile-pics")
    amount_contributed = models.FloatField(default=0.0)
    amount_owed = models.FloatField(default=0.0)
    monthly_payment = models.BooleanField(default=False)
    monthly_vote = models.BooleanField(default=False)
    rank = models.CharField(max_length=32, blank=True, null=True)


#auto_now_add=True creates an unmodifiable date when the object is first created. To be able to modify the date, use "default=timezone.now" - from "django.utils.timezone.now()"

class Cause(models.Model):
    name = models.CharField(max_length=128)
    brief_description = models.CharField(max_length=225)
    country = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=255, blank=True)
    duration = models.IntegerField(default=0)
    detail_description = models.TextField()
    cost = models.FloatField()
    cost_breakdown = models.TextField()
    expiration = models.IntegerField(blank=True)
    investigated = models.BooleanField(default=False)
    investigator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'investigator')
    investigation_note = models.CharField(blank=True, max_length=255)
    approved = models.BooleanField(default=False)
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'approver')
    approved_date = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    backers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'backers')
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'voters')
    completed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    closed_note = models.TextField(blank=True)
    closer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'closer')
    closed_date = models.DateTimeField(blank=True, null=True)
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'supervisor')
    coordinator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'coordinator')
    volunteers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'volunteers')
    status = models.CharField(max_length=32)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128)

# A function to create directory where the files would be uploaded to.
def cause_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cause_<id>/<filename>
    return 'main/causes/cause_{0}/{1}'.format(instance.cause.id, filename)

class Cause_file(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    file_type = models.CharField(choices=FILE_TYPES, max_length=32, null=True, blank=True)
    usage = models.CharField(choices=CAUSE_FILES_USAGE, max_length=32, null=True, blank=True)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=cause_directory_path)


class Test(models.Model):
    pic = models.ImageField(blank=True, upload_to="gallery")
