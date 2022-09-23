# Generated by Django 4.0.6 on 2022-09-20 14:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_visitor_bla_visitor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the right format: 05X-XXXXXXX .', regex='^[0][5][0|2|3|4|5|9][-][0-9]{7}$')]),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='url',
            field=models.URLField(),
        ),
    ]
