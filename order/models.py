from django.db import models
from product.models import Product

from account.models import Account, AccountAddress


# from datetime import date
# Create your models here.

class Cart(models.Model):
    code = models.CharField(max_length=20)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.code, self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(AccountAddress, on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=11)
    insert_date = models.DateField()
    receive_date = models.DateField()
    INSERTED = 1
    IN_WAY = 2
    RECEIVED = 3
    STATUS_CHOICES = ((INSERTED, 'سفارش جدید'), (IN_WAY, 'در حال بسته بندی'), (RECEIVED, 'دریافت شده'))
    status = models.IntegerField(choices=STATUS_CHOICES, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}, {self.customer}, {self.status}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.order, self.price, self.count, self.product}'
