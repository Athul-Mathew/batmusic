# Generated by Django 4.1.7 on 2023-04-26 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad_banner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='image2',
        ),
    ]