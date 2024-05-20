'''La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
 Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''


ingredientes_vegetarianos = ['Pimiento', 'Tofu']
ingredientes_no_vegetarianos = ['Peperoni', 'Jamón', 'Salmón']
opcion = ''
pizza = input("¿Quieres una pizza vegetariana? (s/n): ").lower()


if pizza == 's':
  print('Ingredientes vegetarianos disponibles: ')
  for i in ingredientes_vegetarianos:
    print(i)
  opcion = input('Ingresa que ingrediente deseas: ').title()
  print(f'La pizza no es vegetariana y tiene los siguientes ingredientes: Mozarella, tomate y {opcion}')
elif pizza == 'n':
  print('Ingredientes no vegetarianos disponibles: ')
  for i in ingredientes_no_vegetarianos:
    print(i)
  opcion = input('Ingresa que ingrediente deseas: ').title()
  print(f'La pizza no es vegetariana y tiene los siguientes ingredientes: Mozarella, tomate y {opcion}')
else:
  print('Respuesta no válida')





