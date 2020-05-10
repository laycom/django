# Generated by Django 3.0.5 on 2020-05-08 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200508_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_images', to='products.Product'),
        ),
    ]
