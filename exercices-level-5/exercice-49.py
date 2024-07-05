'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no. '''

num = int(input('Introduce un nuermo entero: '))

def es_primo(num):
    if num <= 1:
        return 'No es primo'
    for i in range(2, int(num  ** 0.5) + 1):
        if num % i == 0:
            return 'No es primo'
    return 'Es es primo'

print(es_primo(num))