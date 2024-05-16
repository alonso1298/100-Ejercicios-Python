'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde 
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +52-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el
número de teléfono sin el prefijo y la extensión.'''

telefono = input('Introduce un numero telefonico con el siguiente formato prefijo-número-extension: ')

telefono = telefono.replace('+52-', '')
telefono = telefono.replace('-', '')

print(telefono)

