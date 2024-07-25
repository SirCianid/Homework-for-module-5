class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.name = args[0]
        cls.houses_history.append(obj.name)
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории!')

h1 = House('ЖК Творобушки', 25)
print(House.houses_history)
h2 = House('Хрущевка', 5)
print(House.houses_history)
h3 = House('Небоскреб', 50)
print(House.houses_history)

del(h1)
del(h3)

print(House.houses_history)
