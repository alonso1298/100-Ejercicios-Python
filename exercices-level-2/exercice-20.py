'''Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience
 leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
 el precio habitual de una barra de pan,
 el descuento que se le hace por no ser fresca y el coste final total.'''

precio_pan = 3.49 
descuento_no_fresca = 0.6

barras_vendidas = int(input('Ingresa el numero de barras vendidas: '))
precio_final = (barras_vendidas * precio_pan) 
precio_descuento =  precio_final * descuento_no_fresca
print('El precio de una barra de pan es de 3.49€')
print('El descuento que se le hace por no ser fresca es del 60%')
print(f'El costo final de las {barras_vendidas} barras vendidas es de {precio_descuento}€')