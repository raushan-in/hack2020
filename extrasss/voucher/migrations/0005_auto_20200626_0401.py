# Generated by Django 3.0.7 on 2020-06-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0004_auto_20200626_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='expiry',
            field=models.DateTimeField(),
        ),
    ]
