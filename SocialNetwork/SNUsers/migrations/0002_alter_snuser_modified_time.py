# Generated by Django 4.0.5 on 2022-06-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snuser',
            name='modified_time',
            field=models.CharField(default='06/19/2022 11:48:28 PM', max_length=50),
        ),
    ]
