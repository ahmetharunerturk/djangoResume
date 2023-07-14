from django.shortcuts import render
from .models import Egitim, Deneyim, KisiselBilgiler

def cv_anasayfa(request):
    egitimler = Egitim.objects.all().order_by('-baslangic_tarihi')
    deneyimler = Deneyim.objects.all().order_by('-baslangic_tarihi')
    kisisel_bilgiler = KisiselBilgiler.objects.first()
    return render(request, 'index.html', {'egitimler': egitimler, 'deneyimler': deneyimler, 'kisisel_bilgiler': kisisel_bilgiler})
