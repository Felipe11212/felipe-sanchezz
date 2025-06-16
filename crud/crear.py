from base_datos import productos

def crear_producto():
    id = input("Ingrese ID: ")
    nombre = input("Ingrese nombre: ")
    precio = float(input("Ingrese precio: "))
    producto = {"id": id, "nombre": nombre, "precio": precio}
    productos.append(producto)
    print("Producto creado exitosamente.")
