# Generated by Django 3.0.1 on 2020-07-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_remove_device_api_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sm',
            name='message',
            field=models.CharField(max_length=512),
        ),
    ]
