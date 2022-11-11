from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    id_company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updateted_at = models.DateTimeField()

