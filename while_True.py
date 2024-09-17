import time

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    @classmethod
    def price_cash(cls, car):
        return print(f'Цена {car.brand}а за наличные {car.price}')

    @classmethod
    def price_of_credit(cls, car):
        return print(f'Цена {car.brand}а в кредит {car.price - (car.price // 100 * 10)}')

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Время выполнения функции {func.__name__}: {elapsed_time:.6f} секунд')
        return result
    return wrapper

@time_decorator
def car_sale(car ,type_sale):
    if type_sale.lower() == 'наличные':
        return Car.price_cash(car)
    elif type_sale.lower() == 'кредит':
        return Car.price_of_credit(car)
    else:
        return 'Неизвестный тип продажи'

car_sale(Car(input('Введите марку машины: '), int(input('Введите цену машины: '))), input('Введите метод покупки: '))