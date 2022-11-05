# dictionary comprehension = create dictionaries using a function (just like list comprehension)
# can replace for loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}

cities_temp_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_temp_c = {key: round((value-32) * (5/9)) for (key,value) in cities_temp_f.items()}
# standard dictionary comprehension - applying math to the value to return a new variable

print(cities_temp_c)

weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_places = {key:value for (key,value) in weather.items() if value == 'sunny'}
print(sunny_places)
# you can use the same as above, but apply conditional statement to parse through your dictionary

cities_temp_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key:('Warm' if value >= 60 else 'Cold') for (key,value) in cities_temp_f.items()}
print(desc_cities)
# you can use if else statement to check values in dictionary.

def check_temp(value):
    if value >= 70:
        return 'HOT'
    elif 69 >= value >= 40:
        return 'WARM'
    else:
        return 'COLD'

cities_temp_f = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities_temp_f.items()}
print(desc_cities)
# Same as aboove but you can pass in a function.

