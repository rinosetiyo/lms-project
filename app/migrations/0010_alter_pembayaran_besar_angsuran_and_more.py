# Generated by Django 4.0.3 on 2023-10-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_pembayaran_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaran',
            name='besar_angsuran',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pembayaran',
            name='jumlah_pembayaran',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
