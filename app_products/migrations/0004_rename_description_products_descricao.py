# Generated by Django 4.2.7 on 2023-11-10 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_alter_products_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='description',
            new_name='descricao',
        ),
    ]