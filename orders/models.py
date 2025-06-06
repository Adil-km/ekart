from django.db import models

# Create your models here.
from customers.models import Customer
from products.models import Product

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE =((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_PROCESSED, "ORDER_PROCESSED"),
                     (ORDER_DELIVERED, "ORDER_DELIVERED"),
                     (ORDER_REJECTED, "ORDER_REJECTED"),)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    total_price = models.FloatField(default=0)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, related_name='order')
    delete_status = models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        owner_name = self.owner.name if self.owner else "NoOwner"
        return "order-{}-{}".format(self.id, owner_name)

class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='added_cart')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='added_items')