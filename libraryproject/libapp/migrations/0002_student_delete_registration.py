# Generated by Django 5.0.6 on 2024-06-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('confirm_password', models.CharField(max_length=128)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science Engineering'), ('EC', 'Electronics and Communication'), ('EEE', 'Electrical and Electronics Engineering'), ('BCA', 'Bachelor of Computer Applications'), ('OTHER', 'Other')], max_length=200)),
                ('roll_number', models.IntegerField()),
                ('registered_id', models.CharField(max_length=10)),
                ('college_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]