from rest_framework import serializers
from .models import Product

def validate_title(value):
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

