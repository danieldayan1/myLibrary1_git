# Generated by Django 4.0.6 on 2022-09-30 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0006_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='borrow_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 30, 13, 47, 28, 413614, tzinfo=utc)),
        ),
    ]