from django import forms
from .models import Brand,Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


# class BrandForm(forms.Form):
#     name = forms.CharField()


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
        fields = ['name']