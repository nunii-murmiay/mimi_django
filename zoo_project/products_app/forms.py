from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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
        fields = ['text', 'rating', 'tovar']


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['name', 'description', 'discount', 'start_date', 'end_date', 'is_active']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Логин пользователя",
        widget=forms.TextInput(attrs={'class':'form-control',}),
        min_length=2
    )
    email = forms.CharField(
        label="Email пользователя",
        widget=forms.EmailInput(attrs={'class':'form-control',}),
    )
    password1 = forms.CharField(
        label="Придумайте пароль",
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
    label="Логин пользователя",
    widget=forms.TextInput(attrs={'class':'form-control',}),
    min_length=2
)
    password = forms.CharField(
    label="Введите пароль",
    widget=forms.PasswordInput(attrs={'class':'form-control',}),

)
    
class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, label='Количество',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}),)
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
        )

