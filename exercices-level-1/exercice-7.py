'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def es_palindromo(palabra):
    palabra_inversa = palabra[::-1]
    cadena_sin_espacio = palabra_inversa.replace(" ", "").lower()
    palabra_sin_espacos = palabra.replace(" ", "").lower()
    if cadena_sin_espacio == palabra_sin_espacos:
        return 'Es palindromo'
    else:
        return 'No es palindromo'
    
print (es_palindromo("oso"))