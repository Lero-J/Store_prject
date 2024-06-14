from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Store(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, related_name='stores', null=True, blank=True)


    class Meta:
        verbose_name = 'Магаз'
        verbose_name_plural = 'Магазы'

    def __str__(self):
        return self.name
