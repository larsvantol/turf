# Generated by Django 4.1.7 on 2023-05-14 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 9, 28, 49, 563819, tzinfo=datetime.timezone.utc), help_text='Date of the transaction.'),
        ),
    ]