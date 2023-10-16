from django.shortcuts import render, redirect, get_object_or_404
from app.models import Tugas, Pembayaran, Jadwal, Pelajaran, Kelas
from django.utils import dates, timezone
from django.contrib.auth.decorators import login_required


def buat_jadwal(request):
    if request.POST:
        hari = request.POST['hari']
        jam = request.POST['jam']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        kelas = Kelas.objects.get(nama_kelas = request.POST['kelas'])

        jadwal = Jadwal.objects.create(hari=hari, jam=jam, pelajaran=pelajaran, kelas=kelas,)
        jadwal.save()
    return redirect('jadwal')

def perbarui_jadwal(request):
    if request.POST:
        hari = request.POST['hari']
        jam = request.POST['jam']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        kelas = Kelas.objects.get(nama_kelas = request.POST['kelas'])

        jadwal = Jadwal.objects.update(hari=hari, jam=jam, pelajaran=pelajaran, kelas=kelas,)
        jadwal.save()
    return redirect('jadwal')

def hapus_jadwal(request, jadwal_id):
    jadwals = get_object_or_404(Jadwal, id=jadwal_id)
    jadwals.delete
    return redirect('jadwal')

def jadwal(request):
    jadwals = Jadwal.objects.all().order_by('hari')
    pelajaran = Pelajaran.objects.values_list('judul_pelajaran', flat=True).distinct()
    kelas = Kelas.objects.values_list('nama_kelas', flat=True).distinct()
    context = {
        'jadwals':jadwals,
        'pelajaran':pelajaran,
        'kelas':kelas,
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
