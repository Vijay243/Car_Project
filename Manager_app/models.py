from django.db import models

class Car_Model(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_model = models.CharField(unique=True,max_length=30)
    c_name= models.CharField(max_length=30)
    c_milege = models.IntegerField()
    c_advance = models.FloatField()
    c_rent_price = models.FloatField()
    c_day_price = models.FloatField()
    c_image = models.ImageField(upload_to='cars_images/')
    def __str__(self):
        return self.c_model
class Driver_Model(models.Model):
    d_id = models.IntegerField(unique=True)
    d_name= models.CharField(max_length=30)
    d_licence = models.CharField(max_length=30,unique=True)
    d_age = models.IntegerField()
    d_gender = models.CharField(max_length=20)
    d_expireance = models.IntegerField()
    d_mobile = models.IntegerField(primary_key=True)
    d_email = models.EmailField(max_length=40,unique=True)
    d_address = models.CharField(max_length=100)
    d_image = models.ImageField(upload_to='driver_images/')
    d_car = models.ManyToManyField(Car_Model)