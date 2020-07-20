from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    title = models.CharField('Название товара', max_length=120)
    description = models.TextField('Описание')
    img_front = models.ImageField(blank=True, upload_to='products/')
    img_back = models.ImageField(blank=True, upload_to='products/')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField('Отображение товара', default=True)
    quantity = models.IntegerField('Количество', default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ItemsSlider(models.Model):
    title = models.CharField('Название товара', max_length=120)
    description = models.TextField('Описание')
    img = models.ImageField(blank=True, upload_to='items_slider/')
    is_active = models.BooleanField('Отображение товара', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объекты для слайдера'
        verbose_name_plural = 'Объекты для слайдера'
        