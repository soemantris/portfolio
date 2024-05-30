from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email','nm_lengkap','no_hp','alamat',)

admin.site.register(Account, AccountAdmin)
admin.site.site_title = 'Sumantri S'
admin.site.site_header = 'Admin Portopolio'