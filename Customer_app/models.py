from django.db import models

class Customer_Model(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=30)
    u_gender = models.CharField(max_length=20)
    u_address = models.CharField(max_length=200)
    u_mobile = models.IntegerField(unique=True)
    u_email = models.EmailField(max_length=30,unique=True)
    u_password = models.CharField(max_length=30)
