'''Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y 
muestre por pantalla su producto escalar.'''

vector1 = [1,2,3]
vector2 = [-1,0,2]

producto_escalar = sum(i * j for i, j in zip(vector1, vector2))

print(f'El producto esclar es: {producto_escalar}')