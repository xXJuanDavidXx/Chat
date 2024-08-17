# Generated by Django 5.1 on 2024-08-14 12:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nombre')),
                ('users', models.ManyToManyField(blank=True, related_name='rooms_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
