from search.client import *

def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop('tags') or []
        if len(tags) != 0:
            params ['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items()]
    if len(index_filters) != 0:
        params['facetFilters'] = index_filters
    results = index.search(query, params)
    return results

