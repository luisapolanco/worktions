# Generated by Django 4.1.6 on 2023-03-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0018_remove_service_category_id_service_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='images',
            field=models.ImageField(null=True, upload_to='media/services/images'),
        ),
    ]
