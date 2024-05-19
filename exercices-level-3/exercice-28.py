'''Escribir un programa que pregunte por consola el precio de un
 producto en pesos con dos decimales y muestre por pantalla el número de pesos y 
el número de centavos del precio introducido.'''

precio_producto = float(input('Ingresa el precio de un producto: '))

pesos = int(precio_producto)
centavos = precio_producto - pesos

print(f'El precio en pesos es de: {pesos}')
print(f'Los centavos son: {round(centavos,2)}')

