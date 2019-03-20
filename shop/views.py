from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'shop/home.html', {})

def info(request):
    products = Product.objects.all()
    return render(request, 'shop/info.html', {'products':products})

def detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/detail.html', {'product':product})
