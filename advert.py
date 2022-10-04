import keyword
from typing import Any


class Dict:
    def __init__(self, json: dict, is_keyword=lambda x: keyword.iskeyword(x)):
        assert isinstance(json, dict)
        self._json = json
        self._is_keyword = is_keyword

    def __underlying(self, attrname: str) -> str:
        if attrname[-1] == "_" and self._is_keyword(attrname[:-1]):
            return attrname[:-1]

        return attrname

    def __getattr__(self, attrname: str) -> Any:
        underlying = self.__underlying(attrname)
        attr = self._json.get(underlying)
        if attr is None:
            return attr

        value = Dict(attr) if isinstance(attr, dict) else attr
        setattr(self, attrname, value)
        return getattr(self, attrname)


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self, text):
        return f"\033[1;{self.repr_color_code};40m {text}\n"


class Advert(ColorizeMixin, Dict):
    def __init__(self, json: dict):
        super().__init__(json, lambda x: keyword.iskeyword(x) or x == "price")
        if self.price is None:
            self.price = 0

    def __repr__(self):
        advert = f"{self.title} | {self.price} ₽"
        return super().__repr__(advert)

    @property
    def price(self):
        if self.price_ < 0:
            raise ValueError("must be >= 0")
        return self.price_

    @price.setter
    def price(self, ad_price):
        if ad_price < 0:
            raise ValueError("must be >= 0")

        self.price_ = ad_price
