# Generated by Django 2.2.4 on 2021-11-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211108_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
