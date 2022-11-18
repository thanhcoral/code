# Generated by Django 4.0.7 on 2022-11-18 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_remove_task_invnetory_task_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='warehouse',
        ),
        migrations.AddField(
            model_name='team',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.warehouse'),
        ),
    ]
