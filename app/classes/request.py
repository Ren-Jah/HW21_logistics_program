class Request:
    def __init__(self, data):  #data - передаваемая пользователем строка
        self.data = self._split_info(data)
        self.from_value = self.data[4]
        self.to_value = self.data[6]
        self.amount = int(self.data[1])
        self.product = self.data[2]

    @staticmethod
    def _split_info(data):
        return data.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_value} в {self.to_value}'