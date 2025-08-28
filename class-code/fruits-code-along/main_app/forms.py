from django import forms
from .models import Fruit

class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name','is_ready_to_eat']