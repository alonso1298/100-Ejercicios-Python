'''Escribir un programa que pida al usuario una palabra y muestre por pantalla
 el número de veces que contiene cada vocal.'''

palabra = input('Ingresa una palabra: ').lower()

vocalesContador = {'a' : 0, 'e': 0, 'i' : 0, 'o' : 0, 'u' : 0}

for letra in palabra: 
    if letra in vocalesContador: 
        vocalesContador[letra] += 1

for vocal, cuenta in vocalesContador.items():
    print(f'La vocal {vocal} aparece {cuenta} veces')