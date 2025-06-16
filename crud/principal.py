from crear import crear_producto
from mostrar import mostrar_productos
from eliminar import eliminar_producto
from actualizar import actualizar_producto

def menu():
    while True:
       
        print("1. Crear producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
