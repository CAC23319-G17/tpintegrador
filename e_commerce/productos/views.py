from django.shortcuts import render
import requests

# Create your views here.

def prod_all(request):
    if 'SITE_NAME' in request.session:
        datos = {}
        datos['SITE_NAME'] = request.session['SITE_NAME']
        datos['COUNT_CART'] = request.session['COUNT_CART']
    request.session.modified = True
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()
    context = {
        'data': products,
        'sesion': datos,
    }
    return render(request, 'productos/index.html', context)

def prod_pop(request):
    if 'SITE_NAME' in request.session:
        datos = {}
        datos['SITE_NAME'] = request.session['SITE_NAME']
        datos['COUNT_CART'] = request.session['COUNT_CART']
    request.session.modified = True
    response = requests.get('https://fakestoreapi.com/products?limit=8')
    products = response.json()
    context = {
        'data': products,
        'sesion': datos,
    }
    return render(request, 'productos/index.html',context=context)

def prod_news(request):
    if 'SITE_NAME' in request.session:
        datos = {}
        datos['SITE_NAME'] = request.session['SITE_NAME']
        datos['COUNT_CART'] = request.session['COUNT_CART']
    request.session.modified = True
    response = requests.get('https://fakestoreapi.com/products?sort=asc')
    products = response.json()
    context = {
        'data': products,
        'sesion': datos,
    }
    return render(request, 'productos/index.html',context=context)