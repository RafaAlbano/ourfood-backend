from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
path("api/media/", include(uploader_router.urls)),


urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)