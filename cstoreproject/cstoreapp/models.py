from django.db import models


# Create your models here.
class foam(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=50)
    courses = models.CharField(max_length=10)
    purpose = models.CharField(max_length=50)
    materials = models.CharField(max_length=50)


    def __str__(self):
        return self.name