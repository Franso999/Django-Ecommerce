# Generated by Django 2.2.4 on 2021-11-08 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20210907_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('company_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('contact_landline', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, null=True, region=None)),
                ('contact_mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, null=True, region=None)),
                ('address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('address_2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('province', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('zip', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('position', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
