from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length = 50)
    email = models.CharField(max_length =30)
    city = models.CharField(max_length =20)
    phone = models.CharField(max_length =15)
    gender = models.CharField(max_length=15)
    user_name = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=50, default='')


class Contractor(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length =50)
    email = models.CharField(max_length = 30)
    city = models.CharField(max_length = 20)
    phone = models.CharField(max_length =15)
    gender = models.CharField(max_length=15)
    user_name = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=50, default='')
 

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25)


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    contractor_id = models.ForeignKey(Contractor, null= False, blank=False, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, null= False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length = 250, default='')
    images = models.ImageField()
