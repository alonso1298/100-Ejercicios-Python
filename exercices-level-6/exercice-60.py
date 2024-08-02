'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''

palabra = input('Ingresa una palabra: ')

palabraInvertida = palabra[::-1]

if palabra == palabraInvertida:
    print('Es palindromo')
else:
    print('No es palindromo')

