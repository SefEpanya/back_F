# Generated by Django 4.0.4 on 2022-05-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifi', '0003_rename_fullname_registration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
