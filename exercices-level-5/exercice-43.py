'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 la cuenta atrás desde ese número hasta cero separados por comas.'''

numero = int(input('Ingresa un nuero entero positivo: '))

while numero >= 0:
    print(numero, end=', ')
    numero -= 1
    
