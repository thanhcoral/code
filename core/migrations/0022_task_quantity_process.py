# Generated by Django 4.0.7 on 2022-11-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_manufacturingplan_planned_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='quantity_process',
            field=models.IntegerField(default=0),
        ),
    ]