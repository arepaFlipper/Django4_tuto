from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import  IsAdminUser
from .models import Product
from api.mixins import StaffEditorPermissionMixin
from .serializers import ProductSerializer

class ProductListCreateAPIView(ListCreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    def get_queryset(self, *args, **kwargs):
        request = self.request
        user = request.user
        print("""🩸   \x1b[1;36;40mviews.py:21  user:""") ## DELETEME
        print(user) ## DELETEME
        print('\x1b[0m') ## DELETEME
        return super().get_queryset(*args,**kwargs)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(StaffEditorPermissionMixin, RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(StaffEditorPermissionMixin, UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()
