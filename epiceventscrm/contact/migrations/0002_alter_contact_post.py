# Generated by Django 3.2.4 on 2021-06-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='post',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('COMMERCIAL', 'COMMERCIAL'), ('SUPPORT', 'SUPPORT')], max_length=20),
        ),
    ]
