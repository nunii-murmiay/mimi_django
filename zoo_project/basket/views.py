from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from products_app.models import Order, Pos_order, Tovar
from products_app.forms import OrderForm, BasketAddProductForm
from .basket import Basket


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Tovar, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product, count=cd['count'], update_count=cd['reload'])
    return redirect('basket_detail')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Tovar, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('tovar_list')

    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            buyer_firstname=form.cleaned_data['buyer_firstname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_surname=form.cleaned_data['buyer_surname'],
            comment=form.cleaned_data['comment'],
            delivery_address=form.cleaned_data['delivery_address'],
            delivery_type=form.cleaned_data['delivery_type'],
            user=request.user,
        )
        for item in basket:
            Pos_order.objects.create(
                tovar=item['product'],
                count=item['count'],
                order=order,
            )
        basket.clear()
        return redirect('basket_detail')
    return redirect('order_open')


@login_required
def open_order(request):
    basket = Basket(request)
    context = {
        'form_order': OrderForm(),
        'basket': basket,
    }
    return render(request, 'order/order_form.html', context)


@login_required
def my_orders(request):
    order_list = Order.objects.filter(user=request.user).order_by('-date_create')
    return render(request, 'order/my_orders.html', {'order_list': order_list})