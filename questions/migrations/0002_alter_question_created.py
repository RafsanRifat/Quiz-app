# Generated by Django 4.0.1 on 2022-01-25 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
