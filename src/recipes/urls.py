from django.urls import path
from .views import home, recipes, recipe_detail

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/', recipe_detail, name='recipe_detail'),
    path('list/', recipes, name='recipes_list'),
]