from django.http import JsonResponse
from django.views import View
from .models import Vendor

class VendorsView(View):
    def get(self, request):
        term = request.GET.get('term', '')
        vendors = Vendor.objects.filter(name__icontains=term).values('id', 'name')

        vendors_data = [
            {
                'id': vendor['id'],
                'label': vendor['name'],
                'value': vendor['name']
            }
            for vendor in vendors
        ]

        return JsonResponse(vendors_data, safe=False)
