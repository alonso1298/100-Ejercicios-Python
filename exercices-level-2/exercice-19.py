'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad
 de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
 Redondear cada cantidad a dos decimales.'''
 
cantidad = int(input('Ingresa el monto a depositar: '))

ahorros = cantidad * 0.4
 
print(f'La cantidad para el primer año es de: {round(ahorros, 2)}')
print(f'La cantidad para el sgundo año es de: {round((ahorros * 2), 2)}')
print(f'La cantidad para el tercer año es de: {round((ahorros * 3), 2)}')
 