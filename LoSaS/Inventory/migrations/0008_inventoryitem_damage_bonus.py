# Generated by Django 4.2.4 on 2023-09-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_remove_inventoryitem_item_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='damage_bonus',
            field=models.IntegerField(null=True),
        ),
    ]