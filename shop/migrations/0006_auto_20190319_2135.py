# Generated by Django 2.1.7 on 2019-03-19 19:35

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190314_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=shop.models.save_image),
        ),
        migrations.AddField(
            model_name='product',
            name='real',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Real'),
            preserve_default=False,
        ),
    ]
