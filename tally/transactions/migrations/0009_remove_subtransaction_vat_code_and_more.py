# Generated by Django 4.1.7 on 2023-05-03 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_subtransaction_account_code_subtransaction_vat_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtransaction',
            name='vat_code',
        ),
        migrations.AddField(
            model_name='subtransaction',
            name='vat_percentage',
            field=models.IntegerField(default=0, help_text='BTW percentage of the transaction.'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 15, 1, 11, 250434, tzinfo=datetime.timezone.utc), help_text='Date of the transaction.'),
        ),
    ]