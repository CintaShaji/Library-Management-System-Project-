# Generated by Django 5.0.6 on 2024-06-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available_copies',
            field=models.PositiveIntegerField(default=1),
        ),
    ]