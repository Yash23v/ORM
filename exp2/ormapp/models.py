from django.db import models
from django.contrib import admin
class CarInventory(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    manufacture_date = models.DateField()
    colour = models.CharField(max_length=30)

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('name','model','price','manufacture_date','colour')
