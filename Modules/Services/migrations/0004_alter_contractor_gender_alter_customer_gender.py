# Generated by Django 4.1.6 on 2023-02-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_alter_contractor_password_alter_contractor_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='gender',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=15),
        ),
    ]
