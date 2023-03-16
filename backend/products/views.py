from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import  IsAdminUser
from .models import Product
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .serializers import ProductSerializer

# class ProductListCreateAPIView( ListCreateAPIView, UserQuerySetMixin):
class ProductListCreateAPIView( UserQuerySetMixin, ListCreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args,**kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        print(request.user)
        return qs.filter(user=request.user)

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
