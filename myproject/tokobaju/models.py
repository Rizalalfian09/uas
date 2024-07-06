from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama

class Pemasok(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    telepon = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nama

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, related_name='produks', on_delete=models.CASCADE)
    pemasok = models.ForeignKey(Pemasok, related_name='produks', on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)
    tanggal_diubah = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class Penjualan(models.Model):
    produk = models.ForeignKey(Produk, related_name='penjualans', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_penjualan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produk.nama} - {self.jumlah}"
