from django.core.management.base import BaseCommand
from search.client import *

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('query',type=str)
        parser.add_argument('--user',action='store_true', default=False)
        parser.add_argument('--public',action='store_true', default=False)

    def handle(self,*args, **kwargs):
        query = kwargs['query']
        index = get_index()
        params = {}
        tags = ""
        if "tags" in kwargs:
            tags = kwargs.pop('tags') or []
            if len(tags) != 0:
                params ['tagFilters'] = tags
        index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
        if len(index_filters) != 0:
            params['facetFilters'] = index_filters
        results = index.search(query, params)
        print("""🇵🇦   \x1b[1;36;40mperform_search.py:22 results:""") ## DELETEME
        print(results) ## DELETEME
        print('\x1b[0m') ## DELETEME

