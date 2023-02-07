from django.db import models
from product.models import Product

from account.models import Account, AccountAddress


# from datetime import date
# Create your models here.


# class OrderPriceDiscount(models.Model):
#     code = models.CharField(max_length=20)
#     Price = models.IntegerField(default=0)
#     PERCENT = 1
#     PRICE = 2
#     TYPE_CHOICES = ((PERCENT, 'درصدی'), (PRICE, 'ریالی'))
#     type = models.IntegerField(choices=TYPE_CHOICES, blank=True)

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
    discount_code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.pk}, {self.customer}, {self.status}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    count = models.IntegerField()
    price = models.IntegerField()
    price_discount = models.IntegerField(null=True)
    percent_discount = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.order, self.price, self.count, self.product}'
#
#
# class OrderPriceDiscount(models.Model):
#     code = models.CharField(max_length=20)
#     price = models.IntegerField(default=0)
#     given_by = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
#
#     def __str__(self):
#         return f'{self.code, self.price}'

# class OrderDiscount(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.RESTRICT)
#     discount = models.ForeignKey(Discount, on_delete=models.RESTRICT)
#
#     def __str__(self):
#         return f'{self.order, self.discount}'
