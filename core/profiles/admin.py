from django.contrib import admin

from profiles.models import Administrator, Client, Supplier

# Register your models here.
admin.site.register(Administrator)
admin.site.register(Client)
admin.site.register(Supplier)