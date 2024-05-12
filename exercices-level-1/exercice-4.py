'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''

vocales = ['a', 'e', 'i', 'o', 'u']

def volcal(caracter):
    if caracter in vocales:
        return 'Es vocal'
    else:
        return f'La {caracter} no es una vocal'

print(volcal('u'))