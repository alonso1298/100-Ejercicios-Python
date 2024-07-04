'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

contraseniaUsuario = 'S@bss2023.'

contrasenia = ''

while contrasenia != contraseniaUsuario:
    contrasenia = input('Introduce la contraseña: ')
    if contrasenia == contraseniaUsuario:
        print('Acceso concedido')
        break