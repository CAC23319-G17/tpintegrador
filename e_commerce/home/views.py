from django.shortcuts import render
from home.forms import ContactoForm

from datetime import datetime
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if not 'SITE_NAME' in request.session:
        request.session['SITE_NAME'] = '"La Tiendita" SHOP'
        request.session['COUNT_CART'] = 2
        request.session.modified = True
    data = [{"id":1,"name":"Retained cholelithiasis following cholecystectomy","spec":"Drainage of Right Brachial Artery, Open Approach","price":6110.9,"ranking":3.0,"urlimage":155},
            {"id":2,"name":"Other superficial bite of hip, right hip","spec":"Removal of Drainage Device from Cervical Vertebral Disc, Percutaneous Endoscopic Approach","price":6697.15,"ranking":1.4,"urlimage":153},
            {"id":3,"name":"Major laceration of unspecified part of pancreas, sequela","spec":"Bypass Coronary Artery, Two Arteries from Aorta with Autologous Venous Tissue, Open Approach","price":6080.45,"ranking":1.7,"urlimage":299},
            {"id":4,"name":"Other osteonecrosis, left fibula","spec":"Reattachment of Vagina, Open Approach","price":2101.01,"ranking":1.9,"urlimage":284},
            {"id":5,"name":"Corrosion of second degree of left toe(s) (nail), subs","spec":"Insertion of Infusion Device into Left Internal Jugular Vein, Percutaneous Approach","price":8940.23,"ranking":3.0,"urlimage":126},
            {"id":6,"name":"Unsp fx low end unsp tibia, 7thE","spec":"Extraction of Ova, Percutaneous","price":9372.45,"ranking":4.8,"urlimage":311},
            {"id":7,"name":"Disp fx of post pro of unsp talus, subs for fx w delay heal","spec":"Physical Rehabilitation and Diagnostic Audiology, Rehabilitation, Activities of Daily Living Assessment","price":2038.15,"ranking":2.9,"urlimage":416},
            {"id":8,"name":"Acute actinic otitis externa, left ear","spec":"Excision of Vulva, Open Approach","price":7005.51,"ranking":3.7,"urlimage":196},
            ]
    context = {
        'data': data,
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

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