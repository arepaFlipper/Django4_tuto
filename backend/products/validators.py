from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title_no_hello(value):
    forbidden_title = "hello"
    if forbidden_title in value.lower():
        raise serializers.ValidationError(f"'{value}' is not allowed")
    return value

unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')
