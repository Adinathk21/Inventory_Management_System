from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json


# Create your views here.
managementjson =settings.MEDIA_ROOT,'management.json'

def management(request):
    try:
        with open(managementjson) as f:
            data=json.load(f)
    except: data = {}

    jsonData = json.dumps(data)

    context = {"jsonData":jsonData}
    context.update(data)
    
    return render(request,'management.html', context)