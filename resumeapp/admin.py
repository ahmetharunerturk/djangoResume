from django.contrib import admin
from .models import Egitim, Deneyim, KisiselBilgiler, Dil
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

admin.site.register(Egitim)
admin.site.register(Deneyim)
admin.site.register(Dil)
admin.site.register(KisiselBilgiler)

