'''Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
 separados por comas, y muestre por pantalla
 cada uno de los productos en una línea distinta.'''
 
productos = input('Ingresa los productos de la cesta de la compra separados por una coma: ')
lista_productos = productos.split(',')

for i in lista_productos:
    print(i.strip())