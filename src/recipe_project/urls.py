from django.contrib import admin
from django.urls import path
from recipes.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),  # Add this line to include the home view
]