# Generated by Django 4.1.6 on 2023-03-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0014_user_delete_customer_service_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='contractor_id',
            new_name='user_id',
        ),
    ]
