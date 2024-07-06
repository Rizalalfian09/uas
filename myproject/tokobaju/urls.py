from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdukViewSet, KategoriViewSet, PemasokViewSet, PenjualanViewSet

router = DefaultRouter()
router.register(r'produks', ProdukViewSet)
router.register(r'kategoris', KategoriViewSet)
router.register(r'pemasoks', PemasokViewSet)
router.register(r'penjualans', PenjualanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
