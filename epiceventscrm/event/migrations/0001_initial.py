# Generated by Django 3.2.4 on 2021-06-17 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('contract', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('event_date', models.DateTimeField()),
                ('attendees', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client')),
                ('contract_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contract.contract')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.status')),
                ('support_contact_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
