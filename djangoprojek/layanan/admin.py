from django.contrib import admin

from .models import Testimony

# Register your models here.
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name','work','review','pub_date')

admin.site.register(Testimony, TestimonyAdmin)