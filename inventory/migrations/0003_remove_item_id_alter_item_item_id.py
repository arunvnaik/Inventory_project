# Generated by Django 5.1.1 on 2024-10-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_item_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
