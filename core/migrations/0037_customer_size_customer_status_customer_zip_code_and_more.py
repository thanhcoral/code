# Generated by Django 4.1.3 on 2022-11-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_component_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='size',
            field=models.CharField(blank=True, choices=[('Cá nhân', 'Cá nhân'), ('Công ty lớn', 'Công ty lớn'), ('Công ty vừa', 'Công ty vừa'), ('Công ty nhỏ', 'Công ty nhỏ'), ('Khác', 'Khác')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Draft', 'Draft'), ('Closed', 'Closed')], default='Active', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('Khách hàng', 'Khách hàng'), ('Khách hàng tiềm năng', 'Khách hàng tiềm năng'), ('Others', 'Others')], default='Khách hàng', max_length=50),
        ),
    ]
