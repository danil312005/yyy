from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('try.urls')),  # Замените <app_name> на имя вашего приложения
]
