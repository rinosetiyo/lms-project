from django.shortcuts import render, redirect, get_object_or_404
from app.models import Tugas, Pembayaran, Jadwal
from django.utils import dates, timezone
from django.contrib.auth.decorators import login_required

# Fungsi untuk membuat pembayaran baru
def jadwal(request):
    jadwals = Jadwal.objects.all().order_by('hari')
    if jadwals.order_by('pelajaran').exists():
        print("True")
    context = {
        'jadwals':jadwals,
    }
    return render(request, 'pages/jadwal.html', context)

def buat_pembayaran(request):
    if request.POST:
        # Ambil data dari form
        jumlah_pembayaran = request.POST['jumlah_pembayaran']
        jumlah_angsuran = request.POST['jumlah_angsuran']
        besar_angsuran = jumlah_pembayaran / jumlah_angsuran
        tanggal_pembayaran = request.POST['tanggal_pembayaran']

        # Buat pembayaran baru
        pembayaran = Pembayaran(
            jumlah_pembayaran=jumlah_pembayaran,
            jumlah_angsuran=jumlah_angsuran,
            besar_angsuran=besar_angsuran,
            tanggal_pembayaran=tanggal_pembayaran,
        )
        pembayaran.save()

        # Kembalikan ke halaman pembayaran
        return redirect('index')
    return render(request, 'pages/buat.html')

# Fungsi untuk membayar angsuran
def bayar_angsuran(request, pk):
    # Cari pembayaran berdasarkan ID
    pembayaran = Pembayaran.objects.get(pk=pk)

    # Perbarui tanggal pembayaran
    pembayaran.tanggal_pembayaran = timezone.now()
    pembayaran.save()

    # Kembalikan ke halaman pembayaran
    return redirect('index')

def index(request):
    all_pembayaran = Pembayaran.objects.all().order_by('-tanggal_pembayaran',)[0:1]
    semua_tugas = Tugas.objects.all()
    jumlah_tugas = semua_tugas.count()

    context = {
        'semuaTugas': semua_tugas,
        'jumlah_tugas': jumlah_tugas,
        'semua_pembayaran': all_pembayaran,
    }
    return render(request, 'pages/index.html', context)
