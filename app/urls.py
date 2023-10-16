from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name="index"),
    path('jadwal/', views.jadwal, name="jadwal"),
    path('jadwal/buat_jadwal', views.buat_jadwal, name="buat_jadwal"),
    path('jadwal/perbarui_jadwal', views.perbarui_jadwal, name="perbarui_jadwal"),
    path('jadwal/hapus_jadwal/<int:jadwal_id>', views.hapus_jadwal, name="hapus_jadwal"),
    path('buat_pembayaran', views.buat_pembayaran, name="buat_pembayaran"),
    path('bayar_angsuran/<int:pk>', views.bayar_angsuran, name="bayar_angsuran"),
]