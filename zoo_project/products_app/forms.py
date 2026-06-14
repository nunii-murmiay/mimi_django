from django import forms
from .models import *


class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = ['name', 'description', 'price', 'photo', 'is_exists', 'category', 'tovartype', 'collection', 'brand']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']


class BrendForm(forms.ModelForm):
    class Meta:
        model = Brend
        fields = ['name', 'description', 'country']


class TovarTypeForm(forms.ModelForm):
    class Meta:
        model = TovarType
        fields = ['name']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'photo', 'preview', 'is_published']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'text', 'rating', 'is_approved', 'tovar']


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name', 'description', 'discount', 'start_date', 'end_date', 'is_active']