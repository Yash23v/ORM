# Ex02 Django ORM Web Application
# Date: 26.11.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import CarInventory, CarInventoryAdmin
admin.site.register(CarInventory, CarInventoryAdmin)

models.py

from django.db import models
from django.contrib import admin
class CarInventory(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    manufacture_date = models.DateField()
    colour = models.CharField(max_length=30)

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('name','model','price','manufacture_date','colour')

```
# OUTPUT
![alt text](<ORM Admin Page SS.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
