from django.db import models

# Create your models here.

class Booking(models.Model):

    name = models.CharField(max_length=40,null=True)
    phone = models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=50,null=True)
    address= models.CharField(max_length=200,null=True)
    item_id= models.CharField(max_length=200,null=True)

    item_name= models.CharField(max_length=200,null=True)
    date_create = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
class name(models.Model):
    name = models.CharField(max_length=40, null=True)

class contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    message = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class product(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    item_id = models.CharField(max_length=200, null=True)

    des = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=20, null=True)
    image = models.ImageField(null=True,blank=True)
    # to make relationship by tag
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.item_name

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('Delivered','Delivered'),
    )
    #to make relationship
    contact = models.ForeignKey(Booking,null=True, on_delete=models.SET_NULL)

    product =models.ForeignKey(product,null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

from django.forms import ModelForm
from .models import Order
class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        # you can use the all and type the one by one
        fields = ['contact','product','status']



