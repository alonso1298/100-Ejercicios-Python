'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

def triangulo(n):
    for i in range(1, n*2, 2):
        fila = [str(j) for j in range(i, 0, -2)]
        print(' '.join(fila))
        
numero = int(input('Introdice un numero entero: '))
print(triangulo(numero))
        