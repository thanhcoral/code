from django.utils import timezone
from django.db import models

CUSTOMER_TYPE = [
    ('Khách hàng', 'Khách hàng'),
    ('Khách hàng tiềm năng', 'Khách hàng tiềm năng'),
]
PRODUCT_TYPE = [
    ('Smartphone', 'Smartphone'),
    ('Laptop', 'Laptop'),
    ('Tablet', 'Tablet'),
]
ORDER_STATUS = [
    ('1', '1'),
    ('2', '2'),
]

class Customer(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    type = models.CharField(max_length=50, choices=CUSTOMER_TYPE, blank=True, null=True)
    def __str__(self):
        return self.name
class CustomerContact(models.Model):
    label = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.customer} [{self.label}]"


class Product(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPE, blank=True, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, blank=True, null=True)
    def __str__(self):
        return f"{self.customer} [{self.order_date.strftime('%d-%m-%y')}]"

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class BOM(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    def __str__(self):
        return self.code

class ManufacturingPlan(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bom = models.ForeignKey(BOM, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

class Team(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Task(models.Model):
    plan = models.ForeignKey(ManufacturingPlan, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

