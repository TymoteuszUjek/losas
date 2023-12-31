# Generated by Django 4.2.4 on 2023-10-14 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0013_item_shop_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blacksmith', '0002_transaction_transaction_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blacksmith_transactions', to='Items.item'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blacksmith_transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
