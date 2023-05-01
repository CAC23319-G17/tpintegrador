from django.shortcuts import render

# Create your views here.


def index(request):
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
        'data': data
    }
    return render(request, 'home/index.html', context)
