# Generated by Django 3.2 on 2021-04-22 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0003_auto_20210421_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='dept',
            new_name='teacher',
        ),
    ]