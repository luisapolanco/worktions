# Generated by Django 4.1.6 on 2023-02-21 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_contractor_password_contractor_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]