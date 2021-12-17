# Generated by Django 4.0 on 2021-12-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=300)),
                ('mobile_number', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
