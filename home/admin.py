from django.contrib import admin

# Register your models here.
from .models import Dealership, Sale, Inventory, Inspection

admin.site.register(Dealership)
admin.site.register(Sale)
admin.site.register(Inventory)
admin.site.register(Inspection)