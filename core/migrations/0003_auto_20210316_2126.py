# Generated by Django 3.1.7 on 2021-03-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210314_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='FromClient',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='message',
            name='ToClient',
            field=models.CharField(max_length=16),
        ),
    ]
