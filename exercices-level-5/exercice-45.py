'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.

*
**
***
****
***** '''

altura = int(input('Introduzca la altura del triángulo: '))

for i in range(1, altura + 1):
    print('*' * i)