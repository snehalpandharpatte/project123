# Generated by Django 3.2 on 2021-04-21 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('College', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='principle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='College.college'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.FloatField()),
                ('salary', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='College.department')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('practical', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subj', to='College.teacher')),
            ],
            options={
                'db_table': 'sub',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('subject', models.ManyToManyField(related_name='stud', to='College.Subject')),
            ],
            options={
                'db_table': 'stud',
            },
        ),
    ]
