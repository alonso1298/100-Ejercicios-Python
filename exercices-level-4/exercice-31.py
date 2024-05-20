'''Escribir un programa que pregunte el nombre el un producto, 
su precio y un número de unidades y muestre por pantalla una cadena con el nombre del 
producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades
 con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
unidades = int(input("Unidades del producto: "))

print(f'El nombre del producto es: {producto}')
print(f'El precio unitario del producto es: {round(precio, 2)}')
print(f'El numero de unidades del producto es: {unidades}')
print(f'El coste total del producto es: {round(precio * unidades, 2)}')