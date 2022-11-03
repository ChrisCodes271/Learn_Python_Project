class Car:
    color = None


class Motorcycle:
    color = None


def change_color(vehicle, color):  # ensure the method you create is outside of the class "Car"

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

motorcycle_1 = Motorcycle()

change_color(car_1, 'Red')
change_color(car_2, 'White')
change_color(car_3, 'Blue')
change_color(motorcycle_1, 'Black')

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motorcycle_1.color)

# Logic behind code above the Car class has an attribute color, that attribute is referenced when creating car_1,2,
# or 3. the change_color method accepts car_1,2, or 3 as a value, and then sets it's color you declare in the method
# to the attribute created by the Car class. you can scale this concept by applying the change_color method to
# another class, such as motorcycle.
