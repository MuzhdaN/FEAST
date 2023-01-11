from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


# Create your models here.
class Table(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    guest = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)

    def __str__(self):
        return self.name
