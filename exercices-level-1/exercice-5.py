'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.'''

def suma(lista):
    resultado = 0
    for i in lista:
        resultado += i 
    return resultado

def multiplicacion(lista):
    resultado = 1
    for i in lista:
        resultado = resultado * i 
    return resultado

print(suma([1,2,3,4]))
print(multiplicacion([1,2,3,4]))