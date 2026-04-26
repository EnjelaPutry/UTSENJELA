from django.shortcuts import render

def home(request):
    context = {
        'nama_lengkap': 'ENJELA NUR PRATAMA PUTRI',
        'sub_info': 'Mahasiswi Sains Data',
        'lokasi': 'Salatiga, Jawa Tengah',
        'no_hp': '+62 87797396587',
        'email': 'enjelaputri04@gmail.com',
        'linkedin': 'Enjela Nur Pratama Putri'
    }
    return render(request, 'index.html', context)