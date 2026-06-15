from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from .models import *
from .forms import *


def info_view(request):
    context = {
        'tovar_list': Tovar.objects.all(),
        'promotion_list': Promotion.objects.filter(is_active=True).order_by('-start_date')[:4],
        'collection_list': Collection.objects.all()[:4],
    }
    return render(request, 'info.html', context)


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


@method_decorator(permission_required('products_app.add_tovar'), name='dispatch')
class TovarCreateView(CreateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')


@method_decorator(permission_required('products_app.change_tovar'), name='dispatch')
class TovarUpdateView(UpdateView):
    model = Tovar
    form_class = TovarForm
    template_name = 'tovar/tovar_form.html'
    success_url = reverse_lazy('tovar_list')


@method_decorator(permission_required('products_app.delete_tovar'), name='dispatch')
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


@method_decorator(permission_required('products_app.add_category'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')


@method_decorator(permission_required('products_app.change_category'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')


@method_decorator(permission_required('products_app.delete_category'), name='dispatch')
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
    template_name = 'brend/brend_details.html'
    context_object_name = 'brend'


@method_decorator(permission_required('products_app.add_brend'), name='dispatch')
class BrendCreateView(CreateView):
    model = Brend
    form_class = BrendForm
    template_name = 'brend/brend_form.html'
    success_url = reverse_lazy('brend_list')


@method_decorator(permission_required('products_app.change_brend'), name='dispatch')
class BrendUpdateView(UpdateView):
    model = Brend
    form_class = BrendForm
    template_name = 'brend/brend_form.html'
    success_url = reverse_lazy('brend_list')


@method_decorator(permission_required('products_app.delete_brend'), name='dispatch')
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
    template_name = 'tovartype/tovartype_details.html'
    context_object_name = 'tovartype'


@method_decorator(permission_required('products_app.add_tovartype'), name='dispatch')
class TovarTypeCreateView(CreateView):
    model = TovarType
    form_class = TovarTypeForm
    template_name = 'tovartype/tovartype_form.html'
    success_url = reverse_lazy('tovartype_list')


@method_decorator(permission_required('products_app.change_tovartype'), name='dispatch')
class TovarTypeUpdateView(UpdateView):
    model = TovarType
    form_class = TovarTypeForm
    template_name = 'tovartype/tovartype_form.html'
    success_url = reverse_lazy('tovartype_list')


@method_decorator(permission_required('products_app.delete_tovartype'), name='dispatch')
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


@method_decorator(permission_required('products_app.add_news'), name='dispatch')
class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')


@method_decorator(permission_required('products_app.change_news'), name='dispatch')
class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news_list')


@method_decorator(permission_required('products_app.delete_news'), name='dispatch')
class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')


class ReviewListView(ListView):
    model = Review
    template_name = 'review/reviews_list.html'
    context_object_name = 'review_list'


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/reviews_details.html'
    context_object_name = 'review'


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/reviews_form.html'

    def get_initial(self):
        initial = super().get_initial()
        tovar_id = self.request.GET.get('tovar')
        if tovar_id:
            initial['tovar'] = tovar_id
        return initial

    def get_success_url(self):
        tovar_id = self.request.GET.get('tovar') or self.object.tovar_id
        if tovar_id:
            return reverse_lazy('tovar_detail', kwargs={'pk': tovar_id})
        return reverse_lazy('review_list')


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/reviews_form.html'
    success_url = reverse_lazy('review_list')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/reviews_delete.html'
    success_url = reverse_lazy('review_list')


class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion/promotion_list.html'
    context_object_name = 'promotion_list'


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotion/promotion_details.html'
    context_object_name = 'promotion'


@method_decorator(permission_required('products_app.add_promotion'), name='dispatch')
class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')


@method_decorator(permission_required('products_app.change_promotion'), name='dispatch')
class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = 'promotion/promotion_form.html'
    success_url = reverse_lazy('promotion_list')


@method_decorator(permission_required('products_app.delete_promotion'), name='dispatch')
class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'promotion/promotion_delete.html'
    success_url = reverse_lazy('promotion_list')


class CollectionListView(ListView):
    model = Collection
    template_name = 'collection/collection_list.html'
    context_object_name = 'collection_list'


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection/collection_details.html'
    context_object_name = 'collection'


@method_decorator(permission_required('products_app.add_collection'), name='dispatch')
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')


@method_decorator(permission_required('products_app.change_collection'), name='dispatch')
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')


@method_decorator(permission_required('products_app.delete_collection'), name='dispatch')
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection/collection_delete.html'
    success_url = reverse_lazy('collection_list')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('info_view')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('info_view')
