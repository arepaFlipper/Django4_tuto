from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from products.models import Product

@api_view(["POST"])
def api_home(request, *args,**kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])
    return JsonResponse(data)
