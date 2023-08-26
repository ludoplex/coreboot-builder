from django.http import JsonResponse
from .models import Device

def index(request, vendor_id):
    devices = Device.objects.filter(vendor_id=vendor_id).values('id', 'name')
    devices_data = [{'id': device['id'], 'label': device['name'], 'value': device['name']} for device in devices]
    return JsonResponse(devices_data, safe=False)
