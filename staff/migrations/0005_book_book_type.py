# Generated by Django 4.0.6 on 2022-09-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]