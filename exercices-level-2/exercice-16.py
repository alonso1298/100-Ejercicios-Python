'''Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
 entera respectivamente. '''
 
num1 = int(input('Introduce el primer numero entero: '))
num2 = int(input('Introduce el segundo numero entero: '))

print(f'La division es {num1/num2}, su cociente es de {num1 % num2}')
 
 