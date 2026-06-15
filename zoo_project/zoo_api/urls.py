from .views import *
from rest_framework import routers

urlpatterns = [
    
]

routers = routers.SimpleRouter()#генераия пути для страницы с помощью роутера
routers.register('category', CategoryViewSet, basename='category')
routers.register('collection', CollectionViewSet, basename='collection')
routers.register('tovar', TovarViewSet, basename='tovar')
routers.register('tovartype', TovarTypeViewSet, basename='tovartype')
routers.register('brend', BrendViewSet, basename='brend')
routers.register('news', NewsViewSet, basename='news')
routers.register('promotion', PromotionViewSet, basename='promotion')
routers.register('review', ReviewViewSet, basename='review')

urlpatterns += routers.urls
