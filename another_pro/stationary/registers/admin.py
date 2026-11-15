from django.contrib import admin
from .models import loginModel
# Register your models here.
@admin.register(loginModel)
class loginAdmin(admin.ModelAdmin):
    list_display = ['username' , 'password']