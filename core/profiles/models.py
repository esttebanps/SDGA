from django.db import models
from django.contrib.auth.models import AbstractUser


"""this is the administrator model"""
class Administrator(AbstractUser):
    email       = models.EmailField(max_length=150, unique=True)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username','first_name','password'] 

""" 
this is the DataUser's model.
this model is not in the database.
from this model will be inherited in the Client and Supplier models.
"""
class DataUser(models.Model):
    name      = models.CharField(max_length=50)
    rut       = models.CharField(max_length=50, unique=True)
    phone     = models.CharField(max_length=20)
    city      = models.CharField(max_length=50)
    
    class Meta:
        abstract = True

"""
this is the Client's model
this model inherits from the DataUser model
"""
class Client(DataUser):
    document = models.CharField(max_length=30)
    
"""
this is the Supplier's model
this model inherits from the DataUser model
"""
class Supplier(DataUser):
    web = models.URLField(max_length=200)



    
    
    
