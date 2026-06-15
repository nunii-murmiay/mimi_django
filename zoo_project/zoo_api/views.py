from .serializers import *
from rest_framework import viewsets
from products_app.models import *
from .permission import *



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySeriaizer
    search_fields = ['name', 'description']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSeriaizer
    search_fields = ['name', 'description']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class BrendViewSet(viewsets.ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSeriaizer
    search_fields = ['name', 'description', 'country']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class TovarTypeViewSet(viewsets.ModelViewSet):
    queryset = TovarType.objects.all()
    serializer_class = TovarTypeSeriaizer
    search_fields = ['name']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class TovarViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSeriaizer
    search_fields = ['name', 'description']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSeriaizer
    search_fields = ['title', 'text', 'preview']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSeriaizer
    search_fields = ['author_name', 'text']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSeriaizer
    search_fields = ['name', 'description']
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [SearchFilter]
