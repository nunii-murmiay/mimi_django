from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from .forms import *

def info_view(request):
    return render(request, 'info.html')

def cart_view(request):
    return render(request, 'cart.html')


class TovarListView(ListView):
    model = Tovar
    template_name = 'tovar/tovar_list.html'
    context_object_name = 'tovar_list'

class TovarDetailView(DetailView):
    model = Tovar
    template_name = 'tovar/tovar_detail.html'
    context_object_name = 'tovar'

class TovarCreateView(CreateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')

class TovarUpdateView(UpdateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')

class TovarDeleteView(DeleteView):
    model = Tovar
    template_name = 'tovar/tovar_delete.html'
    success_url = reverse_lazy('tovar_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('category_list')


class BrendListView(ListView):
    model = Brend
    template_name = 'brend/brend_list.html'
    context_object_name = 'brend_list'

class BrendDetailView(DetailView):
    model = Brend
    template_name = 'brend/brend_detail.html'
    context_object_name = 'brend'

class BrendCreateView(CreateView):
    model = Brend
    form_class = BrendForm
    template_name = 'brend/brend_form.html'
    success_url = reverse_lazy('brend_list')

class BrendUpdateView(UpdateView):
    model = Brend
    form_class = BrendForm
    template_name = 'brend/brend_form.html'
    success_url = reverse_lazy('brend_list')

class BrendDeleteView(DeleteView):
    model = Brend
    template_name = 'brend/brend_delete.html'
    success_url = reverse_lazy('brend_list')


class TovarTypeListView(ListView):
    model = TovarType
    template_name = 'tovartype/tovartype_list.html'
    context_object_name = 'tovartype_list'

class TovarTypeDetailView(DetailView):
    model = TovarType
    template_name = 'tovartype/tovartype_detail.html'
    context_object_name = 'tovartype'

class TovarTypeCreateView(CreateView):
    model = TovarType
    form_class = TovarTypeForm
    template_name = 'tovartype/tovartype_form.html'
    success_url = reverse_lazy('tovartype_list')

class TovarTypeUpdateView(UpdateView):
    model = TovarType
    form_class = TovarTypeForm
    template_name = 'tovartype/tovartype_form.html'
    success_url = reverse_lazy('tovartype_list')

class TovarTypeDeleteView(DeleteView):
    model = TovarType
    template_name = 'tovartype/tovartype_delete.html'
    success_url = reverse_lazy('tovartype_list')


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')


class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'review_list'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    success_url = reverse_lazy('review_list')


class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion/promotion_list.html'
    context_object_name = 'promotion_list'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotion/promotion_detail.html'
    context_object_name = 'promotion'

class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')

class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'promotion/promotion_delete.html'
    success_url = reverse_lazy('promotion_list')