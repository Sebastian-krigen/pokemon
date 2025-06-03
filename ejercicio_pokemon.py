import os,msvcrt

menu = """=====menu=====
1. Agregar pokemon
2. Ver pokemones
3. Eliminar pokemon
4. Salir
"""
pokemones = []
while True:
    os.system('cls')
    print(menu)
    opciones = input("ingrese una opcion: ")
    os.system('cls')
    if opciones=='1':
        print("bienvenido al mundo pokemon")
        numero = int(input("ingrese el número de la cantidad de pokemones: "))
        nombre = input("ingrese el nombre de su pokemon: ").strip().lower()
        altura = input("ingrese la altura de su pokemon: ")
        pokemon = {
            "numero": numero,
            "nombre": nombre,
            "altura": altura
        }
        pokemones.append(pokemon)
        print("pokemon guardado con éxito!")
    elif opciones=='2':
        print("ver pokemones")
        for a in pokemones:
            print(f"el numero {a['numero']} nombre de {a['nombre']} altura de {a['altura']}")
    elif opciones=='3':
        for p in pokemones:
            if a ["nombre"] == nombre:
                pokemones.remove
                print(f"{p['nombre']} ha sido eliminado.")
                break
        else:
            print("\nNo hay Pokémon registrados para eliminar.")
    elif opciones=='4':
        print("muchas gracias")
        break
    else:
         print("opciones incorrectas!")
    print("\n...presione una tecla para continuar...")
    msvcrt.getch()
