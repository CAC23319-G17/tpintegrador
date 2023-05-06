from django.shortcuts import render
from home.forms import ContactoForm

from datetime import datetime
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
import requests
# Create your views here.

def index(request):
    if not 'SITE_NAME' in request.session:
        request.session['SITE_NAME'] = '"La Tiendita" SHOP'
        request.session['COUNT_CART'] = 0
    request.session.modified = True
    response = requests.get('https://fakestoreapi.com/products?limit=8')
    products = response.json()
    context = {
        'data': products,
        'sesion': request.session,
    }
    return render(request, 'home/index.html', context)

def about(request):
    request.session['COUNT_CART'] += 1
    context = {
        'data': {},
        'sesion': request.session,
    }
    return render(request, 'home/about.html', context=context)

def contact(request):
    # mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)    
        # mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
        if(contacto_form.is_valid()):  
            messages.success(request,'Hemos recibido tus datos')
            mensaje=f"De: {contacto_form.cleaned_data['nombre']} <{contacto_form.cleaned_data['email']}>\n Asunto: {contacto_form.cleaned_data['asunto']}\n Mensaje: {contacto_form.cleaned_data['mensaje']}"
            mensaje_html=f"""
                <p>De: {contacto_form.cleaned_data['nombre']} <a href="mailto:{contacto_form.cleaned_data['email']}">{contacto_form.cleaned_data['email']}</a></p>
                <p>Asunto:  {contacto_form.cleaned_data['asunto']}</p>
                <p>Mensaje: {contacto_form.cleaned_data['mensaje']}</p>
            """
            asunto="CONSULTA DESDE LA PAGINA - "+contacto_form.cleaned_data['asunto']
            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.RECIPIENT_ADDRESS],
                fail_silently=False,
                html_message=mensaje_html
            )          
        # acción para tomar los datos del formulario
        else:
            messages.warning(request,'Por favor revisa los errores en el formulario')
    else:
        contacto_form = ContactoForm()
    context = {                
            # 'cursos':listado_cursos,                
            'contacto_form':contacto_form
        }
    return render(request, 'home/contact.html', context=context)