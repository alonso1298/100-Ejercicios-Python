'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''

cantidad = float(input('Ingresa la cantidad a invertir: '))
interes = float(input('Ingresa el interes anual: '))
anios = int(input('Ingresa el numero de años: '))
capital = cantidad

if anios != 0:
    for i in range(1, anios + 1):
        capital = capital * (1 + (interes / 100))
        print(f'Capital en el año {i}: {round(capital, 2)}')
else:
    print('Ingresa un numero diferente de 0 para el numero de años')



