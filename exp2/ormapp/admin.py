from django.contrib import admin
from .models import CarInventory, CarInventoryAdmin
admin.site.register(CarInventory, CarInventoryAdmin)

