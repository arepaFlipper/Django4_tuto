from rest_framework.serializers import ModelSerializer
from api.serializers import UserPublicSerializer
from .models import Article

class ArticleSerializer(ModelSerializer):
    author = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Article
        fields = ['pk', 'author','title', 'body']
