from django.contrib import admin

from store.models import Store,Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Store)