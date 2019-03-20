# Generated by Django 2.1.7 on 2019-03-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('birth', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.BooleanField(verbose_name='Пол')),
            ],
        ),
    ]
