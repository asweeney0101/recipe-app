from django.urls import path
from .views import HomeView, RecipesListView, RecipeDetailView, RecipeCreateView

app_name = 'recipes'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipesListView.as_view(), name='recipes_list'),
    path('add/', RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]