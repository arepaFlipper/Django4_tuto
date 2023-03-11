import json
from django.http import JsonResponse

def api_home(request, *args,**kwargs):
    body = request.body
    data = {}
    try:
        data= json.loads(body)
    except Exception as e:
        pass
    print("""😲   \x1b[1;33;40mviews.py:6   body:""") ## DELETEME
    print(body) ## DELETEME
    print('\x1b[0m') ## DELETEME
    print("""🚮   \x1b[1;35;40mviews.py:16  data:""") ## DELETEME
    print(data) ## DELETEME
    print('\x1b[0m') ## DELETEME
    print("""🇿🇦   \x1b[1;37;42mviews.py:18  dict(request.GET):""") ## DELETEME
    print(dict(request.GET)) ## DELETEME
    print('\x1b[0m') ## DELETEME
    print("""🐸   \x1b[1;31;40mviews.py:20  request.GET:""") ## DELETEME
    print(type(request.GET)) ## DELETEME
    print('\x1b[0m') ## DELETEME
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    print("""🐠   \x1b[1;37;40mviews.py:22  data:""") ## DELETEME
    print(data) ## DELETEME
    print('\x1b[0m') ## DELETEME
    return JsonResponse(data)
