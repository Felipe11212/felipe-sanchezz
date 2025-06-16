from base_datos import productos

def eliminar_producto():
    id = input("Ingrese el ID del producto a eliminar: ")
    for p in productos:
        if p["id"] == id:
            productos.remove(p)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")
