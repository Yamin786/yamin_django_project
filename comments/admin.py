from django.contrib import admin
from .models import comment_model

@admin.register(comment_model)
class comment_admin(admin.ModelAdmin):
    list_display = ['user', 'comment_description', 'created_at']
    search_fields = ['user' , 'created_at']