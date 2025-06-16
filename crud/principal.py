from crear import crearPersona
from eliminar import eliminar
from actualizar import actualizar
from mostrar import Mostrar

personas = []
def menu():
    while True:

        print("1. Crear")
        print("2. mostrar")
        print("3. Actualizar ")
        print("4. Eliminar")
        print("5. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            crearPersona()
            
        elif opcion == "2":
            Mostrar()
            
        elif opcion == "3":
            actualizar()
            
        elif opcion == "4":
            eliminar()
            
        elif opcion == "5":
            print("chao")
            break
        else:
            print("paila")


menu()
