'''Escribir un programa que pregunte al usuario la fecha de su 
nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
 Adaptar el programa anterior para que también funcione cuando
 el día o el mes se introduzcan con un solo carácter.'''
 
from datetime import datetime

fecha_nacimiento_str = input('Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ')

fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y')

print(f'El dia es: {fecha_nacimiento.day}')
print(f'El mes es: {fecha_nacimiento.month}')
print(f'El año es: {fecha_nacimiento.year}')

