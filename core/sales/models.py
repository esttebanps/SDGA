from django.db import models

# Create your models here.
class Sale(models.Model):
    amount_sell = models.IntegerField()
    total_price = models.DecimalField(max_digits=19, decimal_places=10)
    fk_client = models.ForeignKey('user.Client', on_delete = models.PROTECT)
    fk_product = models.ForeignKey('inventory.Product', on_delete = models.PROTECT)
    fk_category = models.ForeignKey('inventory.Category', on_delete = models.PROTECT)
    