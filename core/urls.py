from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавляем стандартные маршруты для входа/выхода:
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('forum.urls')), # Ваши текущие маршруты форума
]