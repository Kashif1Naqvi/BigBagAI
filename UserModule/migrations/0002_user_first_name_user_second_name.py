# Generated by Django 4.2.5 on 2023-09-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
