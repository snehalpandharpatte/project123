# Generated by Django 3.2 on 2021-04-11 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_alter_book_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='bookinfo',
        ),
    ]