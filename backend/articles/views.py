from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer
