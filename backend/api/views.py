import json
from django.http import JsonResponse

def api_home(request, *args,**kwargs):
    body = request.body
    data = {}
    try:
        data= json.loads(body)
    except Exception as e:
        raise e
    else:
        pass
    print("""😲   \x1b[1;33;40mviews.py:6   body:""") ## DELETEME
    print(body) ## DELETEME
    print('\x1b[0m') ## DELETEME
    print("""🚮   \x1b[1;35;40mviews.py:16  data:""") ## DELETEME
    print(data) ## DELETEME
    print('\x1b[0m') ## DELETEME
    return JsonResponse({'message': "Hi there, this is your Django API response!!"})
