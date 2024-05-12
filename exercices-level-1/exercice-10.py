'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''

def procedimiento(lista):
    caracter = ''
    for i in lista:
        caracter += '*' * i + '\n'
    return caracter
        
        
print(procedimiento([4, 9, 7]))