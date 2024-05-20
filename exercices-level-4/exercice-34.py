'''Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error. '''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

try:
    resultado = num1/num2
    print(F'El resultado de la division es: {resultado}')
except ZeroDivisionError:
    print(f'No se puede dividir entre 0')