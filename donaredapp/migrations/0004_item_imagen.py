# Generated by Django 5.2 on 2025-05-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaredapp', '0003_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='items/'),
        ),
    ]
