from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name="index"),
    path('buat_pembayaran', views.buat_pembayaran, name="buat_pembayaran"),
    path('bayar_angsuran/<int:pk>', views.bayar_angsuran, name="bayar_angsuran"),
]