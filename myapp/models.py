from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        return reverse("home")

class SubmitWaste(models.Model):
    WASTE_CHOICES= [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
         ('organic','Organic')
        ]
    contact=models.IntegerField(null=True)
    fullname=models.CharField(max_length=25,null=True)
    COMMUNITY_CHOICES= [
            ('household', 'Household'),
            ('industry', 'Industry'),
            ('market', 'Market'),
            ('office', 'Office'),
            ]
    communityName= models.CharField(max_length=1024,choices=COMMUNITY_CHOICES,default='household')
    typeofwaste= models.CharField(max_length=1024,choices=WASTE_CHOICES,default='organic')
    #typeofwaste=models.CharField(max_length=1024)
    address=models.TextField(max_length=1024, blank=True)
    email = models.EmailField( blank=False, max_length=255, null=True,)
    zipcode=models.IntegerField( null=True)
    quantityofwaste=models.TextField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(null=True, editable=False)
    
class CollectWaste(models.Model):
    WASTE_CHOICES= [
        ('plastic', 'Plastic'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
         ('organic','Organic')
        ]
    contact=models.IntegerField(null=True)
    fullname=models.CharField(max_length=25,null=True)
    COMMUNITY_CHOICES= [
            ('household', 'Household'),
            ('industry', 'Industry'),
            ('market', 'Market'),
            ('office', 'Office'),
            ]
    communityName= models.CharField(max_length=1024,choices=COMMUNITY_CHOICES,default='household')
    typeofwaste= models.CharField(max_length=1024,choices=WASTE_CHOICES,default='organic')
    #typeofwaste=models.CharField(max_length=1024)
    address=models.TextField(max_length=1024, blank=True)
    email = models.EmailField( blank=False, max_length=255, null=True,)
    zipcode=models.IntegerField( null=True)
    quantityofwaste=models.TextField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(null=True, editable=False)
    
class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


