# Generated by Django 4.1.7 on 2023-03-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Csv_Task_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pin_code',
            field=models.CharField(default=323223, max_length=8),
        ),
    ]