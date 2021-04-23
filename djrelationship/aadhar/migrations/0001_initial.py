# Generated by Django 3.2 on 2021-04-19 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Adhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.TextField()),
                ('adhar_no', models.TextField(max_length=100)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aadhar.person')),
            ],
        ),
    ]