'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.'''


frase = input('Ingresa una frase: ')
letra = input('Ingresa una letra: ')
listaFrase = list(frase)
letra_repeticion = listaFrase.count(letra)
print(f'La letra "{letra}" se repite {letra_repeticion} veces en la frase')