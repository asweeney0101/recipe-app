from django import forms


class RecipesSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100, 
        label='Search Recipe or Ingredient', 
        widget=forms.TextInput(
            attrs={"placeholder": "Enter a Recipe Name"}
        )    )
