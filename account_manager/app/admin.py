from django.contrib import admin

from .models import TwitterAccounts, Statistics

# Register your models here.
admin.site.register(TwitterAccounts)
admin.site.register(Statistics)
