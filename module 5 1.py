class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors:
            print('Такого этажа нет')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

h1 = House('ЖК Творобушки', 25)
h2 = House('Хрущевка', 5)
h1.go_to(15)
h2.go_to(8)