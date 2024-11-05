from django.urls import path
from .views import recipes, recipe_detail

urlpatterns = [
    path('', recipes, name='recipes'),
    path('<int:id>/', recipe_detail, name='recipe_detail'),
]