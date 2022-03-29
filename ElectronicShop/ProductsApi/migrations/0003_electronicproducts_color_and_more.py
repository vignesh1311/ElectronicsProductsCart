# Generated by Django 4.0.3 on 2022-03-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsApi', '0002_rename_cartitem_electronicproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronicproducts',
            name='Color',
            field=models.CharField(default='NAN', max_length=200),
        ),
        migrations.AddField(
            model_name='electronicproducts',
            name='HDCapacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='electronicproducts',
            name='Processor',
            field=models.CharField(default='NAN', max_length=200),
        ),
        migrations.AddField(
            model_name='electronicproducts',
            name='RAM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='electronicproducts',
            name='Screensize',
            field=models.FloatField(default=0),
        ),
    ]