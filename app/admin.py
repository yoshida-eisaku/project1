from django.contrib import admin
from .models import Item


@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    pass
# Register your models here.
