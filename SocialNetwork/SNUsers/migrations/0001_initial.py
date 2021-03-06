# Generated by Django 4.0.5 on 2022-06-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SNUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100, null=True)),
                ('modified_time', models.CharField(default='06/19/2022 09:32:42 PM', max_length=50)),
                ('blocked', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=10000, null=True)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='SNUsers.snuser')),
            ],
        ),
    ]
