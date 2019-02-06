# Generated by Django 2.1.5 on 2019-02-03 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Product Description'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(default='None', max_length=50, verbose_name='Product Type'),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]