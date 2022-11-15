from django import forms

from core.models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    type = forms.CharField(widget=forms.Select(choices=CUSTOMER_TYPE,attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)

class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContact
        fields = '__all__'
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    label = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)

class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = '__all__'
    order = forms.ModelChoiceField(queryset=Order.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    product = forms.ModelChoiceField(queryset=Product.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),error_messages={
        'unique': 'Sản phẩm đã tồn tại trong đơn hàng.'
    })
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "order_date": DateTimePickerInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',}),
        }
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    status = forms.CharField(widget=forms.Select(choices=ORDER_STATUS,attrs={'class': 'form-control','style': 'width: 50%; display: inline;',},),)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    type = forms.CharField(widget=forms.Select(choices=PRODUCT_TYPE,attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)

class MrpForm(forms.ModelForm):
    class Meta:
        model = ManufacturingPlan
        fields = '__all__'
        widgets = {
            "start_date": DateTimePickerInput(attrs={'class': 'form-control', }),
            "end_date": DateTimePickerInput(attrs={'class': 'form-control', }),
        }
    order = forms.ModelChoiceField(queryset=Order.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    bom = forms.ModelChoiceField(queryset=BOM.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['plan', 'product', 'team', 'quantity', 'planned_start', 'planned_end']
        widgets = {
            "planned_start": DateTimePickerInput(attrs={'class': 'form-control', }),
            "planned_end": DateTimePickerInput(attrs={'class': 'form-control', }),
        }
    plan = forms.ModelChoiceField(queryset=ManufacturingPlan.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    product = forms.ModelChoiceField(queryset=Product.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    team = forms.ModelChoiceField(queryset=Team.objects.all(),widget=forms.Select(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width: 75%; display: inline;',},),)