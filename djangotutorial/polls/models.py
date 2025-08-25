from django.db import models

class Pelanggan(models.Model): 
    STATUS_CHOICES = [
        ('aktif', 'Aktif'),
        ('menunggu', 'Menunggu'),
        ('nonaktif', 'Nonaktif'),
    ]

    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telepon = models.CharField(max_length=20, blank=True, null=True)
    total_pesanan = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='menunggu')

    def __str__(self):
        return f"{self.nama} ({self.kode})"
