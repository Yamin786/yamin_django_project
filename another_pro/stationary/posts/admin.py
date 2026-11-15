from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(postModel)
class postAdmin(admin.ModelAdmin):
    list_display =['heading' , 'texts' , 'image']