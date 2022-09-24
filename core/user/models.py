from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        
class Client(Profile):
    documento = models.CharField(max_length=30)
    
class Supplier(Profile):
    web = models.URLField(max_length=200)
    
    
    
