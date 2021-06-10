# Generated by Django 3.2.4 on 2021-06-10 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('amount', models.FloatField()),
                ('payment_due', models.DateTimeField(blank=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_client_id', to='client.client')),
                ('sales_contact_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_contact_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
