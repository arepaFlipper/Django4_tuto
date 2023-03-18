from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from . import client

class SearchListView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != '0'
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        print("""🇨🇵   \x1b[1;30;41mperform_search.py:23 user:""") ## DELETEME
        print(user,query,public, tag) ## DELETEME
        print('\x1b[0m') ## DELETEME
        return Response(results)
