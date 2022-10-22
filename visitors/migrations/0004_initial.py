# Generated by Django 4.0.6 on 2022-09-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visitors', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('identication', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('published_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]