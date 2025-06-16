from base_datos import productos

def actualizar_producto():
    id = input("Ingrese el ID del producto a actualizar: ")
    for p in productos:
        if p["id"] == id:
            p["nombre"] = input("Nuevo nombre: ")
            p["precio"] = float(input("Nuevo precio: "))
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")
