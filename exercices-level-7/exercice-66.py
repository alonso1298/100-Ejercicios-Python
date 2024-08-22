'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y
 lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
  vive en <dirección> y su número de teléfono es <teléfono>.'''

nombre = input('Intorduce tu nombre: ')
edad = input('Intorduce tu edad: ')
direccion = input('Intorduce tu direccion: ')
telefono = input('Intorduce tu telefono: ')

datos_usuario = {
    'nombre': nombre, 
    'edad': edad,
    'direccion': direccion, 
    'telefono': telefono
}

print(f'{datos_usuario["nombre"]} tienes una edad de: {datos_usuario["edad"]}, tu direccion es: {datos_usuario["direccion"]} y tu telefono es: {datos_usuario["telefono"]}')