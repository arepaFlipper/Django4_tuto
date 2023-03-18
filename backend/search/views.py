from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from . import client

class SearchListView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response('', status=400)
        results = client.perform_search(query)
        return Response(results)
