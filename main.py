from app.classes.request import Request
from app.classes.shop import Shop
from app.classes.store import Store


def logistic():
    while True:
        print('Введите запрос формата: Доставить (количество) (наименование товара) из (склад/магазин) в (магазин/склад)')
        user_input = input('Введите данные:')

        if user_input.lower() == 'стоп' or user_input.lower() == 'stop':
            print('Работа завершена')
            break

        request = Request(user_input)

        store.items = store_items
        shop.items = shop_items

        if request.from_value == request.to_value:
            print('Пункт назначение == Пункт отправки')
            continue

        if request.from_value == 'склад':
            if request.product in store.items:
                print(f'Нужный товар есть в пункте {request.from_value}')
            else:
                print(f'В пункте {request.from_value} нет данного товара ')
                break

            if store.items[request.product] >= request.amount:  # если кол-во товара на складе больше запрошенного
                print(f'Нужное количество есть в пункте {request.from_value}')
            else:
                print(f'В пункте {request.from_value} не хватает {request.amount - store.items[request.product]}')
                break

            if shop.get_free_space >= request.amount:
                print(f'В пункте {request.to_value} достаточно места')
            else:
                print(shop.get_free_space)
                print(f'В пункте {request.to_value} не хватает {request.amount - shop.get_free_space}')
                continue

            if request.to_value == 'магазин' and shop.get_unique_items_count == 5 and request.product not in shop.items:  # количество уникальных товаров в магазина не должно быть больше пяти
                print('В магазине достаточно уникальных товаров')
                continue

            store.remove(request.product, request.amount)
            print(' ')
            print(f'Курьер забрал {request.amount} {request.product} из пункта {request.from_value}')
            print(f'Курьер везет {request.amount} {request.product}  из пункта {request.from_value} в пункт {request.to_value}')
            shop.add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в пункт {request.to_value}')

        else:
            if request.product in shop.items:
                print(f'Нужный товар есть в пункте {request.from_value}')
            else:
                print(f'В пункте {request.from_value} нет данного товара ')
                continue

            if shop.items[request.product] >= request.amount:  # если кол-во товара в магазине больше запрошенного
                print(f'Нужное количество есть в пункте {request.from_value}')
            else:
                print(f'В пункте {request.from_value} не хватает {request.amount - shop.items[request.product]}')
                continue

            if store.get_free_space >= request.amount:
                print(f'В пункте {request.to_value} достаточно места')
            else:
                print(store.get_free_space)
                print(f'В пункте {request.to_value} не хватает {request.amount - store.get_free_space}')
                continue

            shop.remove(request.product, request.amount)
            print(' ')
            print(f'Курьер забрал {request.amount} {request.product} из пункта {request.from_value}')
            print(
                f'Курьер везет {request.amount} {request.product}  из пункта {request.from_value} в пункт {request.to_value}')
            store.add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в пункт {request.to_value}')

        print('\nНа складе:')
        for title, count in store.items.items():
            print(f'{title}: {count}')

        print('\nВ магазине:')
        for title, count in shop.items.items():
            print(f'{title}: {count}')

        break


if __name__ == "__main__":
    store = Store()
    store_items = {'печеньки': 20, 'собачки': 5, 'коробки': 42}

    shop = Shop()
    shop_items = {'печеньки': 3, 'собачки': 1, 'котята': 1, 'пирожки': 1, 'мышата': 1}

    logistic()
