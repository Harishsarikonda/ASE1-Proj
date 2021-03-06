# Generated by Django 2.1.2 on 2018-11-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('0', 'FAILED'), ('1', 'PLACED'), ('2', 'CONFIRMED'), ('3', 'OUT FOR DELIVERY'), ('4', 'DELIVERED')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('1', 'COD'), ('2', 'ONLINE')], default='', max_length=1),
        ),
    ]
