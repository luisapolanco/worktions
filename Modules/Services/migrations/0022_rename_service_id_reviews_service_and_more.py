# Generated by Django 4.1.2 on 2023-04-26 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0021_alter_reviews_calification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='user_id',
            new_name='user',
        ),
    ]
