# Generated by Django 4.0.6 on 2022-09-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_visitor_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
