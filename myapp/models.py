from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255,null=True,blank=True)
    photo = models.ImageField(null=True)


    def __str__(self):
        return f"{self.name} - {self.email}"

