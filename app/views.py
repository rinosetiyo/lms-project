from django.shortcuts import render, redirect, get_object_or_404
from app.models import Tugas, Pembayaran, Jadwal, Pelajaran, Kelas, Materi
from django.utils import dates, timezone
from django.contrib.auth.decorators import login_required

@login_required(login_url= 'login')
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

def buat_jadwal(request):
    if request.POST:
        hari = request.POST['hari']
        jam = request.POST['jam']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        kelas = Kelas.objects.get(nama_kelas = request.POST['kelas'])

        jadwal = Jadwal(hari=hari, jam=jam, pelajaran=pelajaran, kelas=kelas,)
        jadwal.save()
    return redirect('jadwal')

def perbarui_jadwal(request, jadwal_id):
    jadwal = Jadwal.objects.get(id=jadwal_id)
    if request.POST:
        hari = request.POST['hari']
        jam = request.POST['jam']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        kelas = Kelas.objects.get(nama_kelas = request.POST['kelas'])

        jadwal.hari = hari
        jadwal.jam = jam
        jadwal.pelajaran = pelajaran
        jadwal.kelas = kelas
        jadwal.save()
    return redirect('jadwal')

def hapus_jadwal(request, jadwal_id):
    jadwals = Jadwal.objects.get(id=jadwal_id)
    jadwals.delete()
    return redirect('jadwal')

@login_required(login_url='login')
def materi(request):
    materis = Materi.objects.all()
    pelajaran = Pelajaran.objects.values_list('judul_pelajaran', flat=True).distinct()
    context = {
        'materis':materis,
        'pelajaran':pelajaran,
    }
    return render(request, 'pages/materi.html', context)

def buat_materi(request):
    if request.POST:
        judul = request.POST['judul_materi']
        deskripsi = request.POST['deskripsi']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        file = request.FILES['upload_file']

        materi = Materi(judul_materi=judul, deskripsi=deskripsi, pelajaran=pelajaran, file=file,)
        materi.save()
    return redirect('materi')

def perbarui_materi(request, materi_id):
    materi = Materi.objects.get(id=materi_id)
    if request.POST:
        judul = request.POST['judul_materi']
        deskripsi = request.POST['deskripsi']
        pelajaran = Pelajaran.objects.get(judul_pelajaran = request.POST['pelajaran'])
        file = request.FILES['upload_file']

        materi.judul_materi = judul
        materi.deskripsi = deskripsi
        materi.pelajaran = pelajaran
        materi.file = file
        materi.save()
    return redirect('materi')

def hapus_materi(request, materi_id):
    materi = Materi.objects.get(id=materi_id)
    materi.delete()
    return redirect('materi')

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
