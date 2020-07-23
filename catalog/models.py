from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subjects(models.Model):
    name = models.CharField("Тематика", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'


class Size(models.Model):
    name = models.CharField("Размер", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Material(models.Model):
    name = models.CharField("Материал", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Tags(models.Model):
    name = models.CharField("Тэги", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'


class Products(models.Model):
    title = models.CharField('Название товара', max_length=120)
    img_front = models.ImageField(blank=True, upload_to='products/')
    img_back = models.ImageField(blank=True, upload_to='products/')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, verbose_name='Материал', on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField(Subjects, verbose_name='Тематика')
    size = models.ManyToManyField(Size, verbose_name='Размер')
    tags = models.ManyToManyField(Tags, verbose_name='Тэги')
    is_active = models.BooleanField('Отображение товара', default=True)
    quantity = models.IntegerField('Количество', default=1)
    price = models.IntegerField('Цена', default=100)
    date = models.DateField('Дата добавления товара', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ItemsSlider(models.Model):
    title = models.CharField('Название товара', max_length=120)
    img = models.ImageField(blank=True, upload_to='items_slider/')
    is_active = models.BooleanField('Отображение товара', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объекты для слайдера'
        verbose_name_plural = 'Объекты для слайдера'
        