# Generated by Django 4.1.7 on 2023-10-25 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='full_name',
        ),
    ]