# Generated by Django 4.1.3 on 2022-11-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_alter_customer_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(blank=True, default='company_logo/default.jpg', null=True, upload_to='company_logo/'),
        ),
    ]