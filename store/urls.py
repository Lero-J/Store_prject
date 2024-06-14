
from django.urls import path

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/<int:store_id>', views.store_detail, name='store_detail'),
    path('delete_store/<int:store_id>', views.delete_store, name='delete_store'),
    path('delete_cat/<int:category_id>', views.delete_category, name='delete_category'),
    path('delete_product/<int:product_id>', views.delete_product, name='delete_product'),
    path('edit_store/<int:store_id>', views.edit_store, name='edit_store'),
    path('edit_category/<int:category_id>', views.edit_category, name='edit_category'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product'),
    path('add_category', views.add_category, name='add_category'),
    path('add_product', views.add_product, name='add_product'),
    path('add_store', views.add_store, name='add_store'),
]


