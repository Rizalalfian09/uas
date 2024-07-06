from rest_framework import viewsets
from .models import Produk, Kategori, Pemasok, Penjualan
from .serializers import ProdukSerializer, KategoriSerializer, PemasokSerializer, PenjualanSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class PemasokViewSet(viewsets.ModelViewSet):
    queryset = Pemasok.objects.all()
    serializer_class = PemasokSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class PenjualanViewSet(viewsets.ModelViewSet):
    queryset = Penjualan.objects.all()
    serializer_class = PenjualanSerializer
