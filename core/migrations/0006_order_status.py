# Generated by Django 4.1.3 on 2022-11-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_order_orderline'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=50, null=True),
        ),
    ]
