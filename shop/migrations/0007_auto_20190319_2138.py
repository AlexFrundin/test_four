# Generated by Django 2.1.7 on 2019-03-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190319_2135'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='real',
            unique_together={('catalog', 'subcatalog')},
        ),
    ]
