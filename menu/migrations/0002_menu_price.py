# Generated by Django 2.1.7 on 2019-05-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
