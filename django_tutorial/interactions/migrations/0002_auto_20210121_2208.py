# Generated by Django 3.1.5 on 2021-01-21 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interaction',
            options={'ordering': ('created_on',), 'verbose_name': 'Interaction', 'verbose_name_plural': '1. Interactions'},
        ),
    ]
