from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import home
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('recipes/', include('recipes.urls')),
    path('login/', login_view, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)