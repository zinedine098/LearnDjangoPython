from django.contrib import admin
from .models import Pelanggan

@admin.register(Pelanggan)
class PelangganAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'email', 'telepon', 'total_pesanan', 'status')
    search_fields = ('nama', 'email', 'telepon')
    list_filter = ('status',)
