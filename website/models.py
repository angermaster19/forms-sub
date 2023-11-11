import email
from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.fname + " "+ self.lname
    