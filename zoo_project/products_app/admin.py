from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    pass

@admin.register(TovarType)
class TovarTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    pass