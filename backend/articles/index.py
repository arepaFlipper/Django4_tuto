from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Article

@register(Article)
class ArticleIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = ['title', 'body', 'user', 'publish_date', 'endpoint']
    tags= 'get_tags_list'
    settings = {
        'searchableAttributes':['title', 'body'],
        'attributesForFaceting': ['user'],
        'ranking':['asc(publish_date)'],
    }
