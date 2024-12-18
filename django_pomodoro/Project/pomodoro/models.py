from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField() 


class business_profile(models.Model):
    business_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
        
class Contact(models.Model):
    owner = models.ForeignKey(business_profile, on_delete=models.CASCADE, related_name='contacts')
    email = models.CharField(max_length=100)
    number = models.IntegerField()


class address(models.Model):
    business = models.OneToOneField(business_profile, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=100)
    block = models.CharField(max_length=100)


    #def __str__(self):
    #    return f"Your Street is {self.street} and your Block is : {self.block}"

class local_support(models.Model):
    rating = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

class categories(models.Model):
    category = models.CharField(max_length=100)
    businesstype = models.CharField(max_length=100)


    
