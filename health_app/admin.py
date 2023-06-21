from django.contrib import admin

# Register your models here.

from .models import Symptom, Entry
admin.site.register(Symptom)
admin.site.register(Entry)

