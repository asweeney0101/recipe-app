from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/home.html'

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'