# Generated by Django 4.1.4 on 2023-04-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
