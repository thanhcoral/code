from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from core.forms import *

def dashboard(request):
    return render(request, 'dashboard.html')
def inventory_status():
    return 
#############################################################
def customer(request):
    labels = [i[0] for i in CUSTOMER_TYPE]
    data = [Customer.objects.filter(type=label).count() for label in labels]
    total = Customer.objects.all().count()
    return render(request, 'customer/customer.html', {'labels': labels, 'data': data, 'total': total})
def customer_list(request):
    return render(request, 'customer/customer_list.html', {'customers': Customer.objects.all(), })
def customer_detail(request, id):
    return render(request, 'customer/customer_detail.html', {'customer': Customer.objects.get(id=id), })
def customer_delete(request, id):
    try:
        Customer.objects.get(id=id).delete()
        messages.success(request, 'Xoá thành công.')
    except:
        messages.error(request, 'Khách hàng với ID này không tồn tại.')
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
    return render(request, 'product/product_list.html', {'products': Product.objects.all(),})
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
    return render(request, 'product/product_detail.html', {'product': Product.objects.get(id=id),})
#############################################################
def order(request):
    return render(request, 'order/order.html')
def order_list(request):
    return render(request, 'order/order_list.html', {'orders': Order.objects.all(),})
def order_detail(request, id):
    return render(request, 'order/order_detail.html', {'order': Order.objects.get(id=id),})
def order_detail2(request, id):
    return render(request, 'order/order_detail2.html', {'order': Order.objects.get(id=id),})
def order_delete(request, id):
    try:
        Order.objects.get(id=id).delete()
        messages.success(request, 'Xoá thành công.')
    except:
        messages.error(request, 'Đơn hàng với ID này không tồn tại.')
    return redirect('order_list')
def order_add(request, id=None):
    order_form = OrderForm()
    if id is not None:
        order_form = OrderForm(initial={'customer': Customer.objects.get(id=id)})
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order_list')
    return render(request, 'order/order_add.html', {'order_form': order_form,})

def order_line_add(request, id=None):
    order_line_form = OrderLineForm()
    if id is not None:
        order_line_form = OrderLineForm(initial={'order': Order.objects.get(id=id)})
    if request.method == 'POST':
        order_line_form = OrderLineForm(request.POST)
        if order_line_form.is_valid():
            order_line_form.save()
            messages.success(request, 'Thêm thành công.')
        else:
            messages.error(request, order_line_form.errors)
        return redirect('/order_detail2/' + str(id))
    return render(request, 'order_line/order_line_add.html', {'order_line_form': order_line_form,})
def order_line_delete(request, id):
    try:
        order_id = OrderLine.objects.get(id=id).order.id
        OrderLine.objects.get(id=id).delete()
        messages.success(request, 'Xoá thành công.')
    except:
        messages.error(request, 'OrderLine với ID này không tồn tại.')
        return redirect('order_list')
    return redirect('/order_detail2/' + str(order_id))
#############################################################
def mrp(request):
    return render(request, 'mrp/mrp.html')
def mrp_list(request):
    return render(request, 'mrp/mrp_list.html', {'mrps': ManufacturingPlan.objects.all(),})
def mrp_detail(request, id):
    try:
        mrp = ManufacturingPlan.objects.get(order=Order.objects.get(id=id))
    except:
        messages.error(request, 'Chưa có dự án cho đơn đặt hàng này. Vui lòng khởi tạo.')
        return redirect('order_list')
    return render(request, 'mrp/mrp_detail.html', {
        'mrp': mrp,
        'order_lines': Order.objects.get(id=id).orderline_set.all(),
        'tasks': Task.objects.filter(plan=mrp),
    })
def mrp_add(request, id=None):
    if id is None:
        return render(request, 'mrp/mrp_add.html', {'orders': Order.objects.all(),})
    else:
        ManufacturingPlan.objects.create(
            order = Order.objects.get(id=id),
        )
        return redirect('/mrp_detail/' + str(id))
    # mrp_form = MrpForm()
    # if id is not None:
    #     mrp_form = MrpForm(initial={'order': Order.objects.get(id=id)})
    #     order_lines = Order.objects.get(id=id).orderline_set.all()
    # if request.method == 'POST':
    #     mrp_form = MrpForm(request.POST)
    #     if mrp_form.is_valid():
    #         # mrp_form.save()
    #         messages.success(request, 'Thêm thành công.')
    #     else:
    #         messages.error(request, mrp_form.errors)
    #     return redirect('/mrp/' + str(id))
    # return render(request, 'mrp/mrp_add.html', {'mrp_form': mrp_form, 'order_lines': order_lines, })
def mrp_open(request, id):
    mrp = ManufacturingPlan.objects.get(order=Order.objects.get(id=id))
    mrp.status = 'Open'
    mrp.save()
    return redirect('/mrp_detail/' + str(id))
def mrp_close(request, id):
    mrp = ManufacturingPlan.objects.get(order=Order.objects.get(id=id))
    mrp.status = 'Closed'
    mrp.save()
    return redirect('/mrp_detail/' + str(id))
def mrp_process(request, id):
    mrp = ManufacturingPlan.objects.get(id=id)
    tasks = mrp.task_set.all()
    return render(request, 'mrp/mrp_process.html', {'mrp': mrp, 'tasks': tasks, })
def task_add(request, plan_id=None):
    task_form = TaskForm()
    if plan_id is not None:
        task_form = TaskForm(initial={'plan': ManufacturingPlan.objects.get(id=plan_id)})
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            print(task_form.cleaned_data)
            Task.objects.create(
                plan = task_form.cleaned_data['plan'],
                product = task_form.cleaned_data['product'],
                team = task_form.cleaned_data['team'],
                quantity = task_form.cleaned_data['quantity'],
                start_date = task_form.cleaned_data['planned_start'],
                end_date = task_form.cleaned_data['planned_end'],
                planned_start = task_form.cleaned_data['planned_start'],
                planned_end = task_form.cleaned_data['planned_end'],
            )
            return redirect('/task_add')
    return render(request, 'task/task_add.html', {'task_form': task_form,})
def task_delete(request, id):
    try:
        plan_id = Task.objects.get(id=id).plan.id
        Task.objects.get(id=id).delete()
        messages.success(request, 'Xoá thành công.')
    except:
        messages.error(request, 'Task với ID này không tồn tại.')
    return redirect('/mrp_detail/'+ str(plan_id))
#########################################################################
def mf(request):
    return render(request, 'mf/mf.html', {'products': Product.objects.all(),})
def mf_detail(request, id):
    return render(request, 'mf/mf_detail.html', {'product': Product.objects.get(id=id),})

