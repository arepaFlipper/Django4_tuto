from rest_framework.authtoken.models import *
locals()
Token
dir(Token.objects.all().first())
token_obj = Token.objects.first()
token_obj.created
