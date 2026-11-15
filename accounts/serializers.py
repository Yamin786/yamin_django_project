from rest_framework import serializers
from django.contrib.auth.models import User

class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Only expose public, non-sensitive fields
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
