# Generated by Django 4.1.7 on 2023-10-29 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_product_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="unique_id",
            field=models.IntegerField(null=True),
        ),
    ]
