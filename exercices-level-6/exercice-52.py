'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca
 hasta que el usuario escriba “salir” que terminará.'''

while True:
    ingreso = input('Ingresa texto: ')
    print(f'eco: {ingreso}')
    salida = input('Presiona S para salir u otra tecla para continuar: ').lower()
    if salida == 's':
        break