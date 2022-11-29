# Generated by Django 4.0.7 on 2022-11-29 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_alter_customer_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='chip',
            new_name='components',
        ),
        migrations.RemoveField(
            model_name='product',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='product',
            name='screen',
        ),
        migrations.CreateModel(
            name='GoodsDispatchNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]
