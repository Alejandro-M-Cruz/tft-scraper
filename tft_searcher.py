from typing import Iterable

from tft import TFT


class TFTSearcher:
    def __init__(self, tfts: Iterable[TFT] | str, query: str):
        self.tfts = tfts
        self.query = query

    def search(self) -> list[TFT]:
        return [tft for tft in self.tfts if tft.contains_query(self.query)]
