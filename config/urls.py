from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from ourfood.views import CategoriaViewSet, ProdutoViewSet, ClienteViewSet, PedidoViewSet, ItemPedidoViewSet, FormaDePagamentoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"produtos", ProdutoViewSet, basename="produtos")
router.register(r"pedidos", PedidoViewSet, basename="pedidos")
router.register(r"clientes", ClienteViewSet, basename="clientes")
router.register(r"itempedidos", ItemPedidoViewSet, basename="itempedidos")
router.register(r"formapagamentos", FormaDePagamentoViewSet, basename="formadepagamentos")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)