from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def __str__(self):
        return self.title


class Product(models.Model):
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def str(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def str(self):
        return self.id
