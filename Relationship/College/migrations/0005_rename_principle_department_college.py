# Generated by Django 3.2 on 2021-04-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0004_rename_dept_subject_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='principle',
            new_name='college',
        ),
    ]