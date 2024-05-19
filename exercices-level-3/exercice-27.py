'''Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.'''

correo = input('Introduce un correo electronico: ')

arroba = correo.find('@')

if arroba != -1:
    
    usuario = correo[0 : arroba]
    nuevo_correo = usuario + '@ceu.es'
    print(f'Su nuevo correo es: \n{nuevo_correo}')
    
else:
    print('Correo no valido')