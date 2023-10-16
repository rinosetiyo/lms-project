from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    nama = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/profiles/%Y/%m/%d', blank=True, null=True)
    is_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_pengajar = models.BooleanField(default=False)

    def __str__(self):
        return self.nama.first_name
    
class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_kelas
    
class Pelajaran(models.Model):
    judul_pelajaran = models.CharField(max_length=250)
    deskripsi = models.TextField()

    def __str__(self):
        return self.judul_pelajaran

class Materi(models.Model):
    judul_materi = models.CharField(max_length=200)
    deskripsi = models.TextField()
    pelajaran = models.ForeignKey(Pelajaran, on_delete=models.CASCADE)
    file = models.FileField(upload_to='document/pdfs/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.judul_materi

class Tugas(models.Model):
    judul_tugas = models.CharField(max_length=200)
    deskripsi = models.TextField()
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    materi = models.ForeignKey(Materi, on_delete=models.CASCADE)
    dibuat = models.DateTimeField(auto_now_add=True)
    diedit = models.DateTimeField(auto_now=True)
    batas_waktu = models.DateTimeField()
    selesai = models.BooleanField(default=False)

    def terlewat(self):
        return timezone.now() > self.batas_waktu

    def __str__(self):
        return self.judul_tugas

class Jadwal(models.Model):
    hari = models.DateField()
    jam = models.TimeField()
    pelajaran = models.ForeignKey(Pelajaran, on_delete=models.CASCADE, default=False)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    materi = models.ForeignKey(Materi, on_delete=models.CASCADE, blank=True, null=True)
    tugas = models.ForeignKey(Tugas, on_delete=models.CASCADE, blank=True, null=True)
    # nama pengajar
    
class Pembayaran(models.Model):
    jumlah_pembayaran = models.IntegerField(null=True, blank=True)
    jumlah_angsuran = models.IntegerField()
    besar_angsuran = models.IntegerField(null=True, blank=True)
    tanggal_pembayaran = models.DateField(null=True, blank=True)