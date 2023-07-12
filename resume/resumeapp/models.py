from django.db import models

class Egitim(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.TextField()
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField(blank=True, null=True)  # Bitiş tarihi opsiyonel

    def __str__(self):
        return self.baslik

class Deneyim(models.Model):
    baslik = models.CharField(max_length=100)
    aciklama = models.TextField()
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField(blank=True, null=True)  # Bitiş tarihi opsiyonel

    def __str__(self):
        return self.baslik

class Dil(models.Model):
    ad = models.CharField(max_length=50)

    def __str__(self):
        return self.ad

class KisiselBilgiler(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    meslek = models.CharField(max_length=50, null=True)
    hakkimda = models.CharField(max_length=250, null=True)
    dogum_tarihi = models.DateField()
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    adres = models.TextField()
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    bilinen_diller = models.ManyToManyField(Dil)

    def __str__(self):
        return self.ad + " " + self.soyad
