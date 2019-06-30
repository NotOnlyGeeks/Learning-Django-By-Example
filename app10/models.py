from django.db import models

# Create your models here.
class User1(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    Pic = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.FirstName



