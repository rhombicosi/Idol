# Generated by Django 3.1 on 2020-08-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0009_auto_20200824_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='chebyshev',
            field=models.FileField(blank=True, upload_to='problems/chebyshev/'),
        ),
    ]
