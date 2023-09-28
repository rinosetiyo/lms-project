# Generated by Django 4.0.3 on 2023-09-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_pembayaran'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pembayaran',
            old_name='total_pembayaran',
            new_name='jumlah_angsuran',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='jenis_pembayaran',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='transaksi_pembayaran',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='besar_angsuran',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='jumlah_pembayaran',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='tanggal_jatuh_tempo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='tanggal_pembayaran',
            field=models.DateField(blank=True, null=True),
        ),
    ]