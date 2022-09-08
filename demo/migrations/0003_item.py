# Generated by Django 4.1 on 2022-08-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_courses_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='boby', max_length=100)),
                ('img', models.ImageField(upload_to='media_imgs')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flavor', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], max_length=100)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
