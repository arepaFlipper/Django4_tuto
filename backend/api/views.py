from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product

@api_view(["GET","POST"])
def api_home(request, *args,**kwargs):
    """
    DRF API View
    """
    if request.method != "POST":
        return Response({"detail":"GET not allowed"}, status=405)
        
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title','price'])
    return Response(data)
