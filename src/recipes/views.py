from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_chart
import pandas as pd


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/home.html'

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RecipeSearchForm(self.request.GET or None)
        context['form'] = form
        recipes = self.get_queryset()
        df = pd.DataFrame(list(recipes.values()))
        chart = get_chart(form.cleaned_data.get('chart_type', '#1'), df)
        context['chart'] = chart
        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


def search_recipes(request):
    form = RecipeSearchForm()
    results = None
    chart = None
    if request.method == 'GET' and 'recipe_name' in request.GET:
        form = RecipeSearchForm(request.GET)
        if form.is_valid():
            recipe_name = form.cleaned_data['recipe_name']
            chart_type = form.cleaned_data['chart_type']
            recipes = Recipe.objects.filter(
                Q(name__icontains=recipe_name) | Q(ingredients__icontains=recipe_name)
            )
            # Convert QuerySet to pandas DataFrame
            df = pd.DataFrame(list(recipes.values()))
            results = df.to_html(classes='table table-striped', index=False)
            chart = get_chart(chart_type, df)
    return render(request, 'recipes/search.html', {'form': form, 'results': results, 'chart': chart})