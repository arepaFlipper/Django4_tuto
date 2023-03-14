from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(ListModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
product_list_view = ProductGenericViewSet.as_view({'get':'list'})
