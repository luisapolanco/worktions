# Generated by Django 4.1.6 on 2023-03-09 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0013_remove_service_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='service',
            name='images',
            field=models.ImageField(null=True, upload_to='services/images'),
        ),
        migrations.AlterField(
            model_name='service',
            name='contractor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
    ]
