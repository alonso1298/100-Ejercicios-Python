'''Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión.'''

cantidad_invertir = float(input('Ingresa una cantidad a invertir: '))
tasa_interes = float(input('Ingresa el interes anual: '))
numero_anios = int(input('Ingresa el numero de años: '))

capital = (numero_anios * tasa_interes) * cantidad_invertir

print(f'La cantidad ${cantidad_invertir} con tasa de interes {tasa_interes} en {numero_anios} años, tendra un rendimiento de: {capital}')