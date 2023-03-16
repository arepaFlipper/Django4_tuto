from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only= True)
    this_is_not_real = serializers.CharField(read_only= True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['username','this_is_not_real','id']

    def get_other_products(self,obj):
        print("""🕢   \x1b[1;34;40mserializers.py:9 obj:""") ## DELETEME
        print(obj) ## DELETEME
        print('\x1b[0m') ## DELETEME
        user = obj
        my_products_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(my_products_qs,many=True, context=self.context).data
