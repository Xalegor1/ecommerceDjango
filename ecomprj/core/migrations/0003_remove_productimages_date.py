# Generated by Django 4.1.4 on 2023-03-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_address_options_remove_product_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='date',
        ),
    ]