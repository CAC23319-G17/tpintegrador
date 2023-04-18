from django.shortcuts import render

# Create your views here.

def index(request):
    baseProduct={
        'id':0,
        'name':'Producto',
        'spec':'Descripcion del Producto',
        'price':1225,
        'ranking':4.5
    }
    data=[baseProduct for i in range(8) ]
    context={
        'data':data
    }
    return render(request,'home/index.html',context)