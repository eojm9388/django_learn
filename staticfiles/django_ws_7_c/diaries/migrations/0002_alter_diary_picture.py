# Generated by Django 4.2.11 on 2024-03-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='picture',
            field=models.ImageField(blank=True, upload_to='%Y/%b/%a'),
        ),
    ]
