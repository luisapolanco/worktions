# Generated by Django 4.1.2 on 2023-02-23 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]