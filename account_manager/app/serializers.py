from rest_framework import serializers
from .models import TwitterAccounts


class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterAccounts
        fields = ('login', 'password', 'email', 'phone', 'is_crypto')
