'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''

def longitud(objeto):
    cantidad = 0
    for i in objeto:
        cantidad += 1
    return cantidad
    
lista = [1, 2, 3, 4, 5]
cadena = "Hola, mundo!"

print("Longitud de la lista:", longitud(lista))
print("Longitud de la cadena:", longitud(cadena))