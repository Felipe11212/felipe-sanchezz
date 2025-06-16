from base_datos import productos

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        for p in productos:
            print(f"ID: {p['id']}, Nombre: {p['nombre']}, Precio: {p['precio']}")
