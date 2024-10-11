
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor +1):
                print(floor)
            else:
                print('Такого этажа не существует')


house1 = House('ЖК Гранель', 18)
house2 = House("ЖК Инновация", 10)

house1.go_to(18)
house2.go_to(11)