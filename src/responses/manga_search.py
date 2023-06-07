from ..schemas.responses import MangaDetail
import json

class MangaSearch:
    def __init__(self, querys):
        keys = MangaDetail.__annotations__.keys()
        self.__response = []
        
        for query in querys:
            query = [*query]
            query.pop(5)
            el = dict(zip(keys, query))
            el["genre"] = json.loads(el["genre"])
            self.__response.append(el)
        
    @property
    def response(self):
        return self.__response