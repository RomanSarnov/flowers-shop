from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=100, default=False)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Product(models.Model):
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField('Скидка в процентах', blank=True, null=True, default=0)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def str(self):
        return self.title

    def get_sale(self):
        return int(self.price * (100 - self.stock) / 100)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def str(self):
        return self.id

class MyUser():
    pass