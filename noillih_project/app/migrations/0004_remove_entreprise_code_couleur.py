# Generated by Django 2.2.16 on 2021-10-09 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211009_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entreprise',
            name='code_couleur',
        ),
    ]
