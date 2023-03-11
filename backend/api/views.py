from django.http import JsonResponse

def api_home(request, *args,**kwargs):
    body = request.body
    print("""😲   \x1b[1;33;40mviews.py:6   body:""") ## DELETEME
    print(body) ## DELETEME
    print('\x1b[0m') ## DELETEME
    return JsonResponse({'message': "Hi there, this is your Django API response!!"})
