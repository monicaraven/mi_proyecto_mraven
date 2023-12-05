from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app_Raven/', include('mi_app_Raven.urls')),
]
