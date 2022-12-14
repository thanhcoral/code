# Generated by Django 4.0.7 on 2022-12-12 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_rename_chip_product_components_remove_product_camera_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Chờ thanh toán', 'Chờ thanh toán'), ('Đã thanh toán', 'Đã thanh toán'), ('Khác', 'Khác')], default='Chờ thanh toán', max_length=50)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.invoice')),
            ],
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product/default.jpg', null=True, upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='components',
            field=models.ManyToManyField(blank=True, null=True, related_name='components', to='core.component'),
        ),
        migrations.DeleteModel(
            name='GoodsDispatchNote',
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
