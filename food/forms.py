from django import forms
from .models import food_item

class FoodForm(forms.ModelForm):
    class Meta:
        model = food_item
        fields = ['food_name','food_desc','food_price','food_image']