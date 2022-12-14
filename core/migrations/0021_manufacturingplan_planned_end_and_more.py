# Generated by Django 4.0.7 on 2022-11-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_task_end_date_task_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturingplan',
            name='planned_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manufacturingplan',
            name='planned_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='planned_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='planned_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
