# Generated by Django 3.2.19 on 2023-08-13 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prosyndic', '0002_auto_20230813_0743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ('-created_at',), 'verbose_name': 'Incident', 'verbose_name_plural': 'Incidents'},
        ),
    ]
