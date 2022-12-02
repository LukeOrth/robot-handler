from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tests/', include('tests.urls')),
    path('admin/', admin.site.urls),
]
