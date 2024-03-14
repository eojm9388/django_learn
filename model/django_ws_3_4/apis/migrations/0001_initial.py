# Generated by Django 4.2.11 on 2024-03-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('api_url', models.CharField(max_length=200)),
                ('documentation_url', models.CharField(max_length=200)),
                ('auth_required', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('additional_info_info', models.TextField()),
            ],
        ),
    ]
