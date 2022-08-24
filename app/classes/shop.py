from abc import ABC

from app.classes.store import Store


class Shop(Store, ABC):
    def __init__(self):
        super().__init__()
        self._capacity = 20
