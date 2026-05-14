class Car:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color

def count_by_color(cars):
    car_dict = {}
    for car in cars:
        if car.color in car_dict:
            car_dict[car.color] += 1
        else:
            car_dict[car.color] = 1
    return  car_dict

car1 = Car(1, "Ford", "green")
car2 = Car(2, "Chevy", "green")
car3 = Car(3, "Ferrari", "red")
car4 = Car(4, "Subaru", "blue")
car5 = Car(5, "Dodge", "gold")
cars = [car1, car2, car3, car4, car5]
print(count_by_color(cars))