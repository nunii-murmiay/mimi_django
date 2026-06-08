from .views import *
from django.urls import path, include

urlpatterns = [
    path('', info_view, name='info_view'),
    path('tovar/', tovar_view, name='tovar_view'),
    path('cart/', cart_view, name='cart_view'),

]