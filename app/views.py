from django.shortcuts import render, redirect
from app.models import Tugas, Pembayaran
from django.utils import dates, timezone
from django.contrib.auth.decorators import login_required

# Fungsi untuk membuat pembayaran baru
def buat_pembayaran(request):
    if request.POST:
        # Ambil data dari form
        jumlah_pembayaran = request.POST['jumlah_pembayaran']
        jumlah_angsuran = request.POST['jumlah_angsuran']
        besar_angsuran = jumlah_pembayaran / jumlah_angsuran
        tanggal_jatuh_tempo = request.POST['tanggal_jatuh_tempo']

        # Buat pembayaran baru
        pembayaran = Pembayaran(
            jumlah_pembayaran=jumlah_pembayaran,
            jumlah_angsuran=jumlah_angsuran,
            besar_angsuran=besar_angsuran,
            tanggal_jatuh_tempo=tanggal_jatuh_tempo,
        )
        pembayaran.save()

        # Kembalikan ke halaman pembayaran
        return redirect('pembayaran')
    return render(request, 'pembayaran/buat.html')

# Fungsi untuk melihat daftar pembayaran
def daftar_pembayaran(request):
    # Cari semua pembayaran
    pembayaran = Pembayaran.objects.all()

    # Render template
    return render(request, 'pembayaran/daftar.html', {'pembayaran': pembayaran})

# Fungsi untuk membayar angsuran
def bayar_angsuran(request, pk):
    # Cari pembayaran berdasarkan ID
    pembayaran = Pembayaran.objects.get(pk=pk)

    # Perbarui tanggal pembayaran
    pembayaran.tanggal_pembayaran = timezone.now()
    pembayaran.save()

    # Kembalikan ke halaman pembayaran
    return redirect('pembayaran')

def index(request):
    semua_tugas = Tugas.objects.all()
    jumlah_tugas = semua_tugas.count()

    context = {
        'semuaTugas': semua_tugas,
        'jumlah_tugas': jumlah_tugas,
    }
    return render(request, 'pages/index.html', context)


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Pembayaran</title>
# </head>
# <body>
#     <h1>Pembayaran</h1>

#     {% if request.user.is_authenticated %}
#         <a href="{% url 'pembayaran:buat' %}">Buat Pembayaran</a>
#     {% endif %}

#     {% if pembayaran %}
#         <table>
#             <tr>
#                 <th>Jumlah Pembayaran</th>
#                 <th>Jumlah Angsuran</th>
#                 <th>Besar Angsuran</th>
#                 <th>Tanggal Jatuh Tempo</th>
#                 <th>Tanggal Pembayaran</th>
#             </tr>
#             {% for pembayaran in pembayaran %}
#                 <tr>
#                     <td>{{ pembayaran.jumlah_pembayaran }}</td>
#                     <td>{{ pembayaran.jumlah_angsuran }}</td>
#                     <td>{{ pembayaran.besar_angsuran }}</td>
#                     <td>{{ pembayaran.tanggal_jatuh_tempo }}</td>
#                     <td>{{ pembayaran.tanggal_pembayaran }}</td>
#                 </tr>
#             {% endfor %}
#         </table>
#     {% endif %}

#     {% if request.user.is_authenticated %}
#         <form action="{% url 'pembayaran:bayar' pk=pembayaran.pk %}" method="post">
#             {% csrf_token %}

#             <button type="submit">Bayar Angsuran</button>
#         </form>
#     {% endif %}
# </body>
# </html>
