# Generated by Django 4.0.3 on 2023-10-03 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_pelajaran_remove_materi_kelas_jadwal'),
    ]

    operations = [
        migrations.AddField(
            model_name='materi',
            name='pelajaran',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.pelajaran'),
        ),
        migrations.AddField(
            model_name='pelajaran',
            name='kelas',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.kelas'),
        ),
    ]
