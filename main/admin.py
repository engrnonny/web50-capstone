from django.contrib import admin

from .models import *

# Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = [
#         'user', 'phone'
#     ]

admin.site.register(User)
admin.site.register(Cause_categorie)
admin.site.register(Cause)
admin.site.register(Cause_file)
admin.site.register(Test)