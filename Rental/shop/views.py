from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/cart_detail.html',
                  {'product': product})


def index_show(request):
    return render(request, 'index.html')


def shortfilms_show(request):
    return render(request, 'shortfilms.html')


def colorgrading_show(request):
    return render(request, 'shortfilms.html')


def rental_show(request):
    return render(request, 'shop.html')


def contacts_show(request):
    return render(request, 'contacts.html')


def form_show(request):
    return render(request, 'form.html')
