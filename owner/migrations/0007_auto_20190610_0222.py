# Generated by Django 2.1.7 on 2019-06-10 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_remove_shop_mastername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuboard',
            name='shopID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.Shop', to_field='shopID'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shopID',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
