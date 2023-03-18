from django.core.management.base import BaseCommand
from search.client import *

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('query',type=str)

    def handle(self,*args, **kwargs):
        query = kwargs['query']
        print("""💡   \x1b[1;37;42mperform_search.py:10 query:""") ## DELETEME
        print(query) ## DELETEME
        print('\x1b[0m') ## DELETEME
        index = get_index()
        print("""🔧   \x1b[1;30;43mperform_search.py:14 index:""") ## DELETEME
        print(index) ## DELETEME
        print('\x1b[0m') ## DELETEME
        params = {}
        tags = ""
        if "tags" in kwargs:
            tags = kwargs.pop('tags') or []
            if len(tags) != 0:
                params ['tagFilters'] = tags
        index_filters = [f"{k}:{v}" for k,v in kwargs.items()]
        print("""🎿   \x1b[1;34;40mperform_search.py:24 index_filters:""") ## DELETEME
        print(index_filters) ## DELETEME
        print('\x1b[0m') ## DELETEME
        if len(index_filters) != 0:
            params['facetFilters'] = index_filters
        results = index.search(query, params)
        print("""☄️   \x1b[1;37;46mperform_search.py:30 results:""") ## DELETEME
        print(results) ## DELETEME
        print('\x1b[0m') ## DELETEME

