# Generated by Django 3.2.4 on 2021-06-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_sales_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('PROSPECT', 'PROSPECT'), ('CLIENT', 'CLIENT')], default='PROSPECT', max_length=20),
        ),
    ]
