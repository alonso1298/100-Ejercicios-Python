'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
las letras de la palabra introducida empezando por la última.
        '''

palabra = input('Ingresa un palabra: ')
palabra_invertida = palabra[::-1].replace(' ', '').lower()
letras = list(palabra_invertida)

print(letras)

