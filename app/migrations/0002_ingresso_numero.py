# Generated by Django 5.0.1 on 2024-04-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresso',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
