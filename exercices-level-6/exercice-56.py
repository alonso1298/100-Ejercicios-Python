'''Escribir un programa que pregunte al usuario los números ganadores de 
la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. '''

numGnadores = input('Introduce los números ganadores de la loteria: ')

listaNumeros = list(numGnadores)

print(sorted(listaNumeros))

