from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

from ourfood.views import CategoriaViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"produtos", ProdutoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)