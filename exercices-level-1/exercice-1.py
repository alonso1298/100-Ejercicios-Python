'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''

def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(max(5,11))
    