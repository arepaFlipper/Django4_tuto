from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args,**kwargs):
    """
    DRF API View
    """
    print("""💬   \x1b[1;34;40mviews.py:10  request:""") ## DELETEME
    print(request) ## DELETEME
    print('\x1b[0m') ## DELETEME
    serializer = ProductSerializer(data=request.data)
    print("""💿   \x1b[1;37;45mviews.py:11  serializer.is_valid():""") ## DELETEME
    print(serializer.is_valid()) ## DELETEME
    print('\x1b[0m') ## DELETEME
    print("""📳   \x1b[1;33;40mviews.py:20  request.data:""") ## DELETEME
    print(request.data) ## DELETEME
    print('\x1b[0m') ## DELETEME
    if serializer.is_valid(raise_exception=True):
        instance= serializer.save()
        print("""☎️   \x1b[1;36;40mviews.py:22  instance:""") ## DELETEME
        print(serializer.data) ## DELETEME
        print('\x1b[0m') ## DELETEME
        return Response(serializer.data)
