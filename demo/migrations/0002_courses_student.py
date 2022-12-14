# Generated by Django 4.1 on 2022-08-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='boby', max_length=100)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='boby', max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('courses', models.ManyToManyField(to='demo.courses')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
