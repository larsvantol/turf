# Generated by Django 4.1.7 on 2023-07-03 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0022_rename_encrypted_uuid_customer_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 8, 46, 13, 168861, tzinfo=datetime.timezone.utc), help_text='Date of the transaction.'),
        ),
    ]