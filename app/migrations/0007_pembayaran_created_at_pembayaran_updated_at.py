# Generated by Django 4.0.3 on 2023-10-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_pembayaran_tanggal_jatuh_tempo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembayaran',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
