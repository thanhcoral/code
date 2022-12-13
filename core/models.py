from django.utils import timezone
from django.db import models
from datetime import datetime, timedelta
from PIL import Image

CUSTOMER_TYPE = [
    ('Khách hàng', 'Khách hàng'),
    ('Khách hàng tiềm năng', 'Khách hàng tiềm năng'),
    ('Others', 'Others'),
]
COMPANY_SIZE = [
    ('Cá nhân', 'Cá nhân'),
    ('Công ty lớn', 'Công ty lớn'),
    ('Công ty vừa', 'Công ty vừa'),
    ('Công ty nhỏ', 'Công ty nhỏ'),
    ('Khác', 'Khác'),
]
CUSTOMER_STATUS = [
    ('Active', 'Active'),
    ('Draft', 'Draft'),
    ('Closed', 'Closed'),
]
PRODUCT_TYPE = [
    ('Smartphone', 'Smartphone'),
    ('Laptop', 'Laptop'),
    ('Tablet', 'Tablet'),
]
COMPONENT_TYPE = [
    ('chip', 'chip'),
    ('camera', 'camera'),
]
ORDER_STATUS = [
    ('1', '1'),
    ('2', '2'),
]
MRP_STATUS = [
    ('Draft', 'Draft'),
    ('Open', 'Open'),
    ('Closed', 'Closed'),
]
INVOICE_STATUS = [
    ('Chờ thanh toán', 'Chờ thanh toán'),
    ('Đã thanh toán', 'Đã thanh toán'),
    ('Khác', 'Khác'),
]

class Customer(models.Model):
    class Meta:
        ordering = ['created_at']
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True, default='company_logo/default.jpg')
    type = models.CharField(max_length=50, choices=CUSTOMER_TYPE, default='Khách hàng')
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, choices=COMPANY_SIZE, blank=True, null=True)
    status = models.CharField(max_length=50, choices=CUSTOMER_STATUS, default='Active')
    note = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name
    @property
    def contact_count(self):
        contacts = self.customer_contact.all()
        total = 0
        for contact in contacts:
            total += 1
        return total
    @property
    def order_count(self):
        orders = self.order_set.all()
        total = 0
        for order in orders:
            total += 1
        return total
    def save(self):
        super().save()
        img = Image.open(self.logo.path)
        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.logo.path)
class CustomerContact(models.Model):
    label = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_contact')
    def __str__(self):
        return f"{self.customer} [{self.label}]"
class Supplier(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Component(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=COMPONENT_TYPE, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPE, blank=True, null=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True, default='product/default.jpg')
    components = models.ManyToManyField(Component, blank=True, null=True, related_name='components')
    def __str__(self):
        return self.name
    def inventory(self):
        ivts =Inventory.objects.filter(product=self)
        total = 0
        for ivt in ivts:
            total += ivt.quantity
        return total
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
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
    bom = models.ForeignKey(BOM, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    planned_start = models.DateTimeField(blank=True, null=True)
    planned_end = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=MRP_STATUS, default='Draft', blank=True, null=True)
    def __str__(self):
        return f"{self.order.customer} [{self.order.order_date.strftime('%d-%m-%y')}]"
    def duration(self):
        return (self.end_date-self.start_date).days
    def progress(self):
        return 0
    def export_ability(self):
        for order_line in self.order.orderline_set.all():
            if order_line.product.inventory() < order_line.quantity:
                return False
        return True
class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def total(self, product_id):
        product = Product.objects.get(id=product_id)
        inventories = Inventory.objects.filter(warehouse=self, product=product)
        x = 0
        for inventory in inventories:
            x += inventory.quantity
        return x
class Team(models.Model):
    name = models.CharField(max_length=50)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
class Task(models.Model):
    plan = models.ForeignKey(ManufacturingPlan, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    quantity_process = models.IntegerField(default=0)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    planned_start = models.DateTimeField(blank=True, null=True)
    planned_end = models.DateTimeField(blank=True, null=True)
    is_start = models.BooleanField(default=False, blank=True, null=True)
    is_end = models.BooleanField(default=False, blank=True, null=True)
    def duration(self):
        return (self.end_date-self.start_date).days
    def progress(self):
        return 1.0*(self.quantity_process/self.quantity)

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=INVOICE_STATUS, default='Chờ thanh toán')
    @property
    def total(self):
        return 0

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


