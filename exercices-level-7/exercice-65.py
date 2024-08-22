'''Escribir un programa que guarde en una variable el
 diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al 
 usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input('Ingrese una divisa porfavor: ')

if divisa in monedas:
    print(f'El simbolo de la divisa es: {monedas[divisa]}')
else: 
    print('La divisa no esta en el diccionario')
