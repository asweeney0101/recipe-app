from django import forms


class RecipesSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100, 
        label='Search for Recipes', 
        widget=forms.TextInput(
            attrs={"placeholder": "Ingredient or Recipe"}
        )    )
