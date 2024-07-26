'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista
 las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas
  que el usuario tiene que repetir.'''

asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
aisgnaturas_a_repetir =  []

calificacion = 0

for asignatura in asignaturas:
    calificacion = int(input(f'Cuanto sacaste en las materia de {asignatura}: '))
    if calificacion <= 5:
        aisgnaturas_a_repetir.append(asignatura)
    
print(f'Deberas recursar las asignaturas: {aisgnaturas_a_repetir}')