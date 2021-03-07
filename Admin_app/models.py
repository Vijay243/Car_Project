
from django.db import models

class Manager_Model(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    expireance = models.IntegerField()
    Mobile = models.IntegerField(unique=True)
    Address = models.TextField(max_length=200)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)
    pic = models.ImageField(upload_to='admin_images/')