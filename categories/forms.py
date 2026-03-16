from django import forms
from categories.models import Category




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'slug', 'image')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category Name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category Description'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category Slug'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

