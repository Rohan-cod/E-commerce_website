from django import forms
from .models import Product

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'brief_desc', 'price', 'full_desc', 'pub_date', 'image']