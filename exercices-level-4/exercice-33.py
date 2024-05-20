'''Escribir un programa que almacene la cadena de caracteres contraseña 
en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. '''

password = 'S@bss2023.'.lower()

usuario_password = input('Ingresa la contraseña: ')

if usuario_password == password:
    print(f'La contraseña es correcta')
else:
    print(f'La contraseña es incorrecta')