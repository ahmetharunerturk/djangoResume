from django.db import models
from ckeditor.fields import RichTextField


class Egitim(models.Model):
    okul = models.CharField(max_length=100)
    aciklama = RichTextField()
    degree = RichTextField(null=True)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField(blank=True, null=True)  # Bitiş tarihi opsiyonel

    def __str__(self):
        return self.okul

class Deneyim(models.Model):
    gorev = models.CharField(max_length=100)
    aciklama = RichTextField()
    firma = RichTextField(null=True)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField(blank=True, null=True)  # Bitiş tarihi opsiyonel

    def __str__(self):
        return self.gorev

class KisiselBilgiler(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    meslek = models.CharField(max_length=50, null=True)
    hakkimda = RichTextField(null=True)
    dogum_tarihi = models.DateField()
    email = models.EmailField()
    cv = models.FileField(upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    telefon = models.CharField(max_length=20)
    adres = models.TextField()
    profile_photo  = models.ImageField(upload_to="media/%Y/%m/%d/", blank=True, null=True)
    background_photo = models.ImageField(upload_to="media/%Y/%m/%d/", blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.ad + " " + self.soyad

class Dil(models.Model):
    ad = models.CharField(max_length=50,blank=True, null=True)
    seviye = models.CharField(max_length=50,blank=True, null=True)
    sertifika = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.ad