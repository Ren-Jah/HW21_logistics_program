from abc import ABC

from app.classes.storage import Storage


class Store(Storage, ABC):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        """функция добавления товара"""
        if title in self._items:
            self._items[title] += count  # увеличиваем кол-во items, если товар уже есть в словаре
        else:
            self._items[title] = count  # иначе просто добавляем в словарь
        self._capacity -= count  # уменьшаем кол-во свободного места

    def remove(self, title, count):
        """функция удаления товара"""
        res = self._items[title] - count
        if res > 0:
            self._items[title] = res  # перезаписываем кол-во items, если остается какое-то кол-во
        else:
            del self._items[title]  # удаляем товар, которого уже нет
        self._capacity += count  # освобождаем кол-во свободного места

    @property
    def get_free_space(self):
        """функция получения свободного места на складе"""
        return self._capacity

    @property
    def items(self):
        """функция получения содержания склада"""
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        """функция получения количества уникальных товаров"""
        return len(self._items.keys())