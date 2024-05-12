'''Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.'''

pago_hora = 60
horas_trabajo = int(input('¿Cuantas horas has trabajado?: '))

print(f'El coste por hora trabajada es de ${pago_hora} has trabajado {horas_trabajo}, su total es de: ${pago_hora * horas_trabajo}')