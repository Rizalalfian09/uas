from rest_framework import serializers
from .models import Produk, Kategori, Pemasok, Penjualan

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class PemasokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemasok
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer()
    pemasok = PemasokSerializer()

    class Meta:
        model = Produk
        fields = '__all__'

class PenjualanSerializer(serializers.ModelSerializer):
    produk = ProdukSerializer()

    class Meta:
        model = Penjualan
        fields = '__all__'
