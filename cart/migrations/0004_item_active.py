# Generated by Django 3.2.5 on 2022-06-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_rename_items_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
