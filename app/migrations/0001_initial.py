# Generated by Django 4.0.3 on 2023-09-21 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kelas', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_materi', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Tugas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_tugas', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dateline', models.DateTimeField()),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kelas')),
                ('materi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materi')),
            ],
        ),
    ]