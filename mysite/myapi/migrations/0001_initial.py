# Generated by Django 3.0.1 on 2020-01-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(blank=True, max_length=60, null=True)),
                ('status', models.IntegerField()),
                ('created_at', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(blank=True, max_length=60, null=True)),
                ('client_id', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Sm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('mobilenumber', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=160)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]