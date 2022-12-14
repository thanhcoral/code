# Generated by Django 4.0.7 on 2022-11-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_manufacturingplan_is_open_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', unique=True)),
            ],
        ),
    ]
