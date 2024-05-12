'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. '''

def max_de_tres(num1, num2, num3):
    if num1 > num2 and num3:
        return num1
    elif num3 > num1 and num2:
        return num3
    elif num2 > num1 and num3:
        return num2
    
print(max_de_tres(9,7,1))