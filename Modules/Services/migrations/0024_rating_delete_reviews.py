# Generated by Django 4.1.2 on 2023-05-24 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0023_user_barrio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
