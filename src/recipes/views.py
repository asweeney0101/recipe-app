from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .models import Recipe
from .forms import RecipesSearchForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/home.html'


        

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipesSearchForm()
        return context
    
    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        recipes = Recipe.objects.filter(name__icontains=search_query)
        # context = super().get_context_data(**kwargs)
        context = {}
        context['form'] = RecipesSearchForm()
        context['recipes'] = recipes
        
        return render(request, self.template_name, context)

        

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'