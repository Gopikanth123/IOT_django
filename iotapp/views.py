# iotapp/views.py
from django.shortcuts import render, HttpResponse
from .models import Testing
import json

def home(request):
    if request.method == 'GET':
        return render(request, 'milk_data_form.html')
    elif request.method == 'POST':
        # Handle data submission from Thonny
        data = json.loads(request.body)
        
        # Save data to the Testing model
        Testing.objects.create(
            can_number=data['can_number'],
            name=data['name'],
            fat=data['fat'],
            snf=data['snf'],
            clr=data['clr'],
            adc_water=data['adc_water']
        )
        
        return HttpResponse(json.dumps({'status': 'success'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'status': 'error', 'message': 'Invalid request method'}), content_type="application/json")
