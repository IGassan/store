from django.db import models


# для того чтобы указать что эти классы будут затем использоваться для создание таблиц БД
# с параметрах указывается models.Model
class ProductCategory(models.Model):
    # так как мы используем эти поля для создания БД(а в них требуется указывать тип данных)
    # мы через класс models указываем тип данных и его параметры
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    # прописываем для изменения отображения в админке
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
