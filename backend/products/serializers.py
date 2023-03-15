from rest_framework import serializers 
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title_no_hello, validate_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')
    title = serializers.EmailField(validators=[validate_title_no_hello, validate_title])
    class Meta:
        model = Product
        fields =[
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def validate_title(self,value):
        request = self.context.get('request')
        print("""📅   \x1b[1;30;43mserializers.py:23    value:""") ## DELETEME
        print(value) ## DELETEME
        print('\x1b[0m') ## DELETEME
        qs = Product.objects.filter(title__iexact=value)
        print("""📺   \x1b[1;33;40mserializers.py:24    qs:""") ## DELETEME
        print(qs) ## DELETEME
        print('\x1b[0m') ## DELETEME
        if qs.exists():
            raise serializers.ValidationError(f'"{value}" is already a product name.')
        return value

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        return reverse("product-edit", kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
