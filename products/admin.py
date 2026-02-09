from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price','created_at']


# Register your models here.
admin.site.register(MenuItem,ItemAdmin)