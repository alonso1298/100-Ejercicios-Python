'''Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.'''

import statistics

numeros = input('Introduce una muestra de numeros separados por comas: ')

lista_numeros = [float(i) for i in numeros.split(',')]

#Se calcula la media 
media = statistics.mean(lista_numeros)

#Se calcula la desviacion tipica
desviacion = statistics.stdev(lista_numeros)

print(f'La media es: {media}')
print(f'La desviación típica es: {desviacion}')