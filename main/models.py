

from django.contrib.auth.models import User
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

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(choices=GENDER, max_length=8, null=True, blank=True)
    title = models.CharField(max_length=6, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=32, blank=True)
    lga = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    occupation = models.CharField(max_length=64, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    linkedin = models.URLField(blank=True)
    followers = models.ManyToManyField(User, related_name = 'followers', blank=True)
    following = models.ManyToManyField(User, related_name = 'following', blank=True)
    profile_picture = models.ImageField(upload_to='main/users/profile-pics/', blank=True)
    amount_contributed = models.FloatField(default=0.0)
    amount_owed = models.FloatField(default=0.0)
    monthly_payment = models.BooleanField(default=False)
    monthly_vote = models.BooleanField(default=False)
    rank = models.CharField(max_length=32, blank=True)


#auto_now_add=True creates an unmodifiable date when the object is first created. To be able to modify the date, use "default=timezone.now" - from "django.utils.timezone.now()"

class Cause(models.Model):
    name = models.CharField(max_length=128)
    brief_description = models.CharField(max_length=225)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=32)
    lga = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    duration = models.IntegerField(default=1)
    detail_description = models.TextField()
    cost = models.FloatField()
    cost_breakdown = models.TextField()
    expiration = models.IntegerField(blank=True)
    status = models.CharField(choices=STATUS, max_length=32, null=True, blank=True)
    investigated = models.BooleanField(default=False)
    investigator = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'investigator')
    investigation_note = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
    approver = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'approver')
    approved_date = models.DateTimeField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    backers = models.ManyToManyField(User, blank=True, related_name = 'backers')
    voters = models.ManyToManyField(User, blank=True, related_name = 'voters')
    completed = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    closed_note = models.TextField(blank=True)
    closer = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'closer')
    supervisor = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'supervisor')
    coordinator = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True, related_name = 'coordinator')
    volunteers = models.ManyToManyField(User, related_name = 'volunteers')
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128)

# A function to create directory where the files would be uploaded to.
def cause_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cause_<id>/<filename>
    return 'causes/cause_{0}/{1}'.format(instance.cause.id, filename)

class Cause_file(models.Model):
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=cause_directory_path)


