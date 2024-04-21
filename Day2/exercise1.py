# Día 2: 30 Días de Programación en Python

name = 'Elsa'
last_name = 'Pallito'
full_name = 'Elsa Pallito'
country = 'Republica Dominicana'
city = 'Santo Domingo'
age = 49
year = 2024
is_married = True
is_true = 'Me gusta el arte'
is_light_on = False
pet, hobbie, favorite_food = '3 michis', 'jugar videojuegos', 'pizza'

print(type(name), len(name), name)
print(type(last_name), len(last_name), last_name)
print(type(full_name), full_name)
print(type(country), country)
print(type(city), city)
print(type(age), age)
print(type(year), year)
print(type(is_married), is_married)
print(type(is_true), is_true)
print(type(is_light_on), is_light_on)
print(type(pet), pet)
print(type(hobbie), hobbie)
print(type(favorite_food), favorite_food)

num_one = 5
num_two = 4
suma = num_one + num_two
print(suma)
resta = num_one - num_two
print(resta)
multiplicacion = num_one * num_two
print(multiplicacion)
division = num_one / num_two
print(division)
modulo = num_one % num_two
print(modulo)
potencia = num_one**num_two
print(potencia)
division_piso = num_one // num_two
print(division_piso)

radio = 30
area_de_circulo = 3.14 * radio * radio
print(area_de_circulo)
circunferencia = 2 * 3.14 * radio
print(circunferencia)

radio_usuario = float(input("ingresa el radio del circulo: "))
area_usuario = 3.14 * radio_usuario * radio_usuario
print(area_usuario)

user_name = input("Ingresa tu nombre: ")
user_last_name = input("Ingresa tu apellido: ")
user_country = input("Ingresa tu país: ")
user_age = int(input("Ingresa tu edad: "))
print(user_name)
print(user_last_name)
print(user_country)

help('keywords')