from car import Car

car_1 = Car('Chevy', 'Corvette', '2021', 'Blue')
car_2 = Car('Ford', 'Mustang', '2022', 'Red')

car_2.wheels = 2 #this will modify the class variable for car_2 only.

print(car_1.wheels) #this will show you the class variable set for car_1
print(car_2.wheels)

print(Car.wheels) #this will show you the class variable

Car.wheels = 6 #this will change the class variable default. It will NOT overwrite established variables from above

print(car_1.wheels) #this will show you the class variable set for car_1
print(car_2.wheels)

print(Car.wheels) #this will show you the class variable
