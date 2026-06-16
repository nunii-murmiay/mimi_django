from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MAX_LEGHT = 255
class Category(models.Model):
    name = models.CharField(max_length=MAX_LEGHT, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):#что будет отображаться   
        return self.name
    class Meta:#то как будет отображаться у админа
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(max_length=MAX_LEGHT, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Brend(models.Model):
    name = models.CharField(max_length=MAX_LEGHT, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    country = models.CharField(max_length=MAX_LEGHT, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class TovarType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название типа')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'

class Tovar(models.Model):
    name = models.CharField(max_length=MAX_LEGHT, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField( verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')#куда именно загрузится картинка внутри проекта
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    tovartype = models.ForeignKey(TovarType, on_delete=models.PROTECT, verbose_name='Тип товара')
    collection = models.ManyToManyField(Collection, verbose_name='Коллекция', blank=True)
    brand = models.ForeignKey(Brend, on_delete=models.PROTECT, verbose_name='Бренд')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class News(models.Model):
    title = models.CharField(max_length=MAX_LEGHT, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='news/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    preview = models.TextField(null=True, blank=True, verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Promotion(models.Model):
    name = models.CharField(max_length=MAX_LEGHT, verbose_name='Название акции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    discount = models.PositiveIntegerField(verbose_name='Размер скидки %')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    tovar = models.ManyToManyField(Tovar, blank=True, verbose_name='Товары по акции')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

class Review(models.Model):
    author_name = models.CharField(max_length=MAX_LEGHT, verbose_name='Имя автора')
    text = models.TextField(null=True, blank=True, verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка', choices=[(i, i) for i in range(1, 6)])
    is_approved = models.BooleanField(default=False, verbose_name='Одобрен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE, verbose_name='Товар', related_name='reviews')

    def __str__(self):
        return f"Отзыв от {self.author_name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Order(models.Model):

    
    SHOP = 'SH'
    COURIER = 'CR'
    PICKUPPOINT = 'PP'
    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]
    

    buyer_firstname = models.CharField(max_length=MAX_LEGHT, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LEGHT, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LEGHT, blank=True, null=True, verbose_name='Отчество покупателя')
    comment = models.CharField(max_length=MAX_LEGHT, blank=True, null=True, verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LEGHT, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tovar = models.ManyToManyField(Tovar, through='Pos_order', verbose_name='Товар')
    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Pos_order(models.Model):
    tovar = models.ForeignKey(Tovar, on_delete=models.PROTECT, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    def __str__(self):
        return f'Заказ №{self.order.pk} - {self.tovar.name} ({self.order.buyer_firstname})'
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'