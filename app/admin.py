from django.contrib import admin
from app.models import Kelas, Materi, Tugas, Pembayaran, Pelajaran, Jadwal, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Kelas)
admin.site.register(Materi)
admin.site.register(Tugas)
admin.site.register(Pembayaran)
admin.site.register(Pelajaran)
admin.site.register(Jadwal)