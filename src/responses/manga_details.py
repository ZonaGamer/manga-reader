from ..schemas.responses import MangaDetail
import json

class MangaDetails:
    def __init__(self, query):
        keys = MangaDetail.__annotations__.keys()
        self.__response = dict(zip(keys, query))
        self.__response["genre"] = json.loads(self.__response["genre"])
        
    @property
    def response(self):
        return self.__response