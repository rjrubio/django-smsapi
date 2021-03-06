# Generated by Django 3.0.1 on 2020-07-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_customfcmdevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=512)),
                ('device_model', models.CharField(max_length=128)),
                ('device_manufacturer', models.CharField(max_length=128)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
