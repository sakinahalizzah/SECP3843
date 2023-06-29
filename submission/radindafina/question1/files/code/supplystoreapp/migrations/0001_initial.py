# Generated by Django 4.1.9 on 2023-06-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('saleDate', models.DateTimeField(db_column='sale_date')),
                ('storeLocation', models.CharField(db_column='store_location', max_length=100)),
                ('customerGender', models.CharField(db_column='customer_gender', max_length=1)),
                ('customerAge', models.PositiveIntegerField(db_column='customer_age')),
                ('customerEmail', models.EmailField(db_column='customer_email', max_length=254)),
                ('satisfaction', models.PositiveSmallIntegerField()),
                ('couponUsed', models.BooleanField(db_column='couponUsed')),
                ('purchaseMethod', models.CharField(db_column='purchase_method', max_length=100)),
            ],
        ),
    ]