from django.forms import ModelMultipleChoiceField
from django.shortcuts import render, get_object_or_404, redirect

from store.models import Category, Product, Store


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    stores = Store.objects.all()
    ctx = {
        'products':products,
        'categories':categories,
        'stores':stores
    }
    return render(request, 'store/index.html', context=ctx)



def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    products = store.product.all()
    ctx = {
        'store':store,
        'products':products,
    }
    return render(request, 'store/storeinfo.html', context=ctx)



def edit_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    ctx = {
        'store':store
    }
    store.name = request.POST.get('new_name')
    if store.name != None:
        store.save()
    return render(request,'store/store_edit.html', context=ctx)



def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    ctx = {
        'category':category
    }
    category.name = request.POST.get('new_cat_name')
    if category.name != None:
        category.save()
    return render(request,'store/cat_edit.html', context=ctx)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    ctx = {
        'product':product
    }
    product.name = request.POST.get('new_product_name')
    if product.name != None:
        product.save()
    return render(request,'store/product_edit.html', context=ctx)


def delete_store(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    store.delete()
    return redirect('index')

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('index')

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('index')


def add_category(request):
    categorie = Category()
    if request.POST.get('cat_name') != None and request.POST.get('cat_name') != "":
        categorie.name = request.POST.get('cat_name')
        categorie.save()
    return render(request, 'store/cat_add.html',context={'cat':categorie})


def add_product(request):
    categories = Category.objects.all()
    product = Product()
    if request.POST.get('NEW_product_name') != None and request.POST.get('NEW_product_name') != "":
        product.name = request.POST.get('product_name')
        product.category = Category.objects.get(name=request.POST.get('NEW_product_name'))
        product.price = request.POST.get('product_price')
        product.save()
    ctx = {
        'categories':categories,
        'product':product
    }
    return render(request,'store/product_add.html',context=ctx)



def add_store(request):
    products = Product.objects.all()
    # print(products)
    store = Store()
    if request.POST.get('NEW_store_name') != None and request.POST.get('store_address') != None:
        store.name = request.POST.get('NEW_store_name')
        store.address = request.POST.get('store_address')
        store.save()
    ctx = {
        'store':store,
        'products' : products
    }
    return render(request, 'store/store_add.html',context=ctx)










