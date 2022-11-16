# Generated by Django 4.0.6 on 2022-11-14 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_alter_book_book_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='books',
        ),
        migrations.AddField(
            model_name='loan',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitors.book'),
        ),
    ]
