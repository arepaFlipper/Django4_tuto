from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print("""🐹   \x1b[1;36;40mviews.py:10  serializer:""") ## DELETEME
        print(serializer.validated_data) ## DELETEME
        print('\x1b[0m') ## DELETEME
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content= instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()

class ProductMixinView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print("""📳   \x1b[1;31;46mviews.py:62  args, kwargs:""") ## DELETEME
        print(args, kwargs) ## DELETEME
        print('\x1b[0m') ## DELETEME
        return self.list(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()
