# Generated by Django 2.1.2 on 2018-10-12 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181012_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='preco',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='titulo',
            new_name='title',
        ),
    ]
