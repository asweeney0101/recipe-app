from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
   return render(request, 'recipes/home.html')

def recipes(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': all_recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

