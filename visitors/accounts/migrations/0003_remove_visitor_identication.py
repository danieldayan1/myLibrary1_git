# Generated by Django 4.0.6 on 2022-11-13 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_visitor_id_alter_visitor_identication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='identication',
        ),
    ]
