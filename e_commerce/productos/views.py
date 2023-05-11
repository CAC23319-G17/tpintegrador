from django.shortcuts import render

# Create your views here.

def productos(request):
    baseProduct={
        'id':0,
        'name':'Producto',
        'spec':'Descripcion del Producto',
        'price':1225,
        'ranking':4.5
    }
    data=[baseProduct for i in range(12) ]
    context={
        'data':data
    }
    return render(request,'productos/al_products.html',context)


def new_arrivals(request):
    context = {

    }
    return render(request, 'porductos/new_arrivals.html', context)