'''Escribir un programa que pida al usuario un número entero positivo
 y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. '''


numero = int(input('Ingresa un numero entero positivo: '))

for i in range(1, numero + 1):
    if numero % 2 != 0:
        print(i, end=(', '))
