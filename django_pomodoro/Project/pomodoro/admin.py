from django.contrib import admin
from django.urls import path,include
from .models import business_profile,Contact,address,local_support,categories,Post
# Register your models here.

admin.site.register([business_profile,Contact,
address,local_support,categories])