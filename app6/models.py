from django.db import models

# Create your models here.
class Users(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    Email=models.EmailField()

    def __str__(self):
        return self.Email
