# Generated by Django 4.0.7 on 2022-11-14 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_orderline_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturingplan',
            name='bom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.bom'),
        ),
    ]
