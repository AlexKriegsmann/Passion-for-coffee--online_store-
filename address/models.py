from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    postal_cod = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    user = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return f'{self.street} {self.number} {self.city}'