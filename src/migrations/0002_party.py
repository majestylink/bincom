# Generated by Django 4.1.5 on 2023-01-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_id', models.CharField(max_length=11)),
                ('party_name', models.CharField(max_length=11)),
            ],
        ),
    ]
