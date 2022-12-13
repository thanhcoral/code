from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),

    path('customer/', customer, name='customer'),
    path('customer/customer_list', customer_list, name='customer_list'),
    path('customer/customer_detail/<int:id>', customer_detail, name='customer_detail'),
    path('customer/customer_delete/<int:id>', customer_delete, name='customer_delete'),
    path('customer/customer_add', customer_add, name='customer_add'),
    path('customer/customer_normal_list', customer_normal_list, name='customer_normal_list'),
    path('customer/customer_potential_list', customer_potential_list, name='customer_potential_list'),
    path('customer/customer_contact_detail/<int:id>', customer_contact_detail, name='customer_contact_detail'),
    path('customer/customer_contact_add', customer_contact_add, name='customer_contact_add'),
    path('customer/customer_contact_add/<int:id>', customer_contact_add, name='customer_contact_add'),
    path('customer/customer_contact_edit/<int:id>', customer_contact_edit, name='customer_contact_edit'),
    path('customer/customer_contact_delete/<int:id>', customer_contact_delete, name='customer_contact_delete'),

    path('product/', product, name='product'),
    path('product/product_add', product_add, name='product_add'),
    path('product/product_list', product_list, name='product_list'),
    path('product/product_detail/<int:id>', product_detail, name='product_detail'),
    path('product/product_delete/<int:id>', product_delete, name='product_delete'),

    path('product/mf', mf, name='mf'),
    path('product/mf_detail/<int:id>', mf_detail, name='mf_detail'),

    path('product/gdn_add/<int:id>', gdn_add, name='gdn_add'),
    path('product/gdn_export/<int:id>', gdn_export, name='gdn_export'),
    path('product/inventory', inventory, name='inventory'),

    path('sales/', order, name='sales'),
    path('sales/order_list', order_list, name='order_list'),
    path('sales/order_detail/<int:id>', order_detail, name='order_detail'),
    path('sales/order_detail2/<int:id>', order_detail2, name='order_detail2'),
    path('sales/order_delete/<int:id>', order_delete, name='order_delete'),
    path('sales/order_add', order_add, name='order_add'),
    path('sales/order_add/<int:id>', order_add, name='order_add'),

    path('sales/order_line_add/<int:id>', order_line_add, name='order_line_add'),
    path('sales/order_line_delete/<int:id>', order_line_delete, name='order_line_delete'),

    path('mrp', mrp, name='mrp'),
    path('mrp/mrp_list', mrp_list, name='mrp_list'),
    path('mrp/mrp_open_list', mrp_open_list, name='mrp_open_list'),
    path('mrp/mrp_closed_list', mrp_closed_list, name='mrp_closed_list'),
    path('mrp/mrp_detail/<int:id>', mrp_detail, name='mrp_detail'),
    path('mrp/mrp_add', mrp_add, name='mrp_add'),
    path('mrp/mrp_add/<int:id>', mrp_add, name='mrp_add'),
    path('mrp/mrp_open/<int:id>', mrp_open, name='mrp_open'),
    path('mrp/mrp_close/<int:id>', mrp_close, name='mrp_close'),
    path('mrp/mrp_process/<int:id>', mrp_process, name='mrp_process'),
    
    path('mrp/task_add', task_add, name='task_add'),    
    path('mrp/task_add/<int:plan_id>/<int:product_id>', task_add, name='task_add'),
    path('mrp/task_delete/<int:id>', task_delete, name='task_delete'),
    path('mrp/task_detail/<int:id>', task_detail, name='task_detail'),
    path('mrp/task_start/<int:id>', task_start, name='task_start'),
    path('mrp/task_update/<int:id>', task_update, name='task_update'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
