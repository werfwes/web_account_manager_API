from django.db import models


# Create your models here.
class TwitterAccounts(models.Model):
    login = models.TextField()
    password = models.TextField()
    email = models.TextField()
    phone = models.TextField(blank=True)
    is_crypto = models.BooleanField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login


class Statistics(models.Model):
    machine_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_id
