from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save#allows us to automaticallly create a new profile when user signsup

# Create your models here.

class ShippingAddress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name=models.CharField(max_length=225)
    shipping_email=models.CharField(max_length=255)
    shipping_address1=models.CharField(max_length=200,blank=True)
    shipping_address2=models.CharField(max_length=200,blank=True)
    shipping_city=models.CharField(max_length=200,blank=True)
    shipping_state=models.CharField(max_length=200,null=True,blank=True)
    shipping_zip=models.CharField(max_length=200,null=True,blank=True)
    shipping_country=models.CharField(max_length=200,blank=True)
    class Meta:
        verbose_name_plural="Shipping Address"

    def __str__(self):
        return f"Shipping Address -{str(self.id)}"
def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping=ShippingAddress(user=instance)
        user_shipping.save()
#automte it
post_save.connect(create_shipping, sender=User)
   
#create order model..overall order
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    shippimg_address=models.TextField(max_length=1500)
    amount_paid=models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order - {str(self.id)}'
    
class OrderItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return f'Order Item - {str(self.id)}'


