from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView, GenericAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser,IsStaffEditorPermission]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

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

