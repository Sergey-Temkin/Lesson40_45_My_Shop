from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from myshop import settings

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/products/
    path('products/', include('products.urls')),
]

# URL pattern for static files(images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)