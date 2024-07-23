class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return str(f'{self.name}, кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Творобушки', 25)
h2 = House('Хрущевка', 5)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))