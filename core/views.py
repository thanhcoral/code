from django.shortcuts import render, redirect

from core.forms import *


def dashboard(request):
    return render(request, 'dashboard.html')

#############################################################
def customer(request):
    return render(request, 'customer/customer.html')
def customer_list(request):
    return render(request, 'customer/customer_list.html', {'customers': Customer.objects.all(), })
def customer_detail(request, id):
    return render(request, 'customer/customer_detail.html', {'customer': Customer.objects.get(id=id), })
def customer_delete(request, id):
    return redirect('customer_list')
def customer_add(request):
    customer_form = CustomerForm()
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer_list')
    return render(request, 'customer/customer_add.html', {'customer_form': customer_form, })
def customer_normal_list(request):
    return render(request, 'customer/customer_normal_list.html', {'normal_customers': Customer.objects.filter(type='Khách hàng'), })
def customer_potential_list(request):
    return render(request, 'customer/customer_potential_list.html', {'potential_customers': Customer.objects.filter(type='Khách hàng tiềm năng'), })

def customer_contact_add(request):
    customer_contact_form = CustomerContactForm()
    if request.method == 'POST':
        customer_contact_form = CustomerContactForm(request.POST)
        if customer_contact_form.is_valid():
            customer_contact_form.save()
            return redirect('customer_list')
    return render(request, 'customer_contact/customer_contact_add.html', {'customer_contact_form': customer_contact_form, })
#############################################################
def product(request):
    return render(request, 'product/product.html')
def product_list(request):
    return render(request, 'product/product_list.html', {
        'products': Product.objects.all(),
    })
def product_add(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_list')
    return render(request, 'product/product_add.html', {
        'product_form': product_form,
    })
def product_detail(request, id):
    return render(request, 'product/product_detail.html', {
        'product': Product.objects.get(id=id),
    })
#############################################################
def order(request):
    return render(request, 'order/order.html')

def order_list(request):
    return render(request, 'order/order_list.html', {
        'orders': Order.objects.all(),
    })

def order_add(request):
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order_list')
    return render(request, 'order/order_add.html', {
        'order_form': order_form,
    })

def order_detail(request, id):
    return render(request, 'order/order_detail.html', {
        'order': Order.objects.get(id=id),
    })