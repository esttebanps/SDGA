from django.db import models

# Create your models here.

class Category(models.Model):
  
    name = models.CharField(max_length=50)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    amount = models.IntegerField()
    discount = models.DecimalField(max_digits=19, decimal_places=10)
    code = models.IntegerField()
    fk_category = models.ForeignKey('Category', on_delete = models.PROTECT)
    fk_supplier = models.ForeignKey('profiles.Supplier', on_delete = models.PROTECT)
    

    