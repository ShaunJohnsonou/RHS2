# Generated by Django 4.2 on 2023-04-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Start_Date',
            field=models.DateField(max_length=50),
        ),
    ]
