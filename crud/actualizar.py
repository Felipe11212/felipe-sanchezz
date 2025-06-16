personas=[]
def actualizar():
    id_persona = int(input("ID de la persona a actualizar: "))
    for persona in personas:
        if persona["id"] == id_persona:
            persona["nombre"] = input("Nuevo nombre: ")
            persona["edad"] = input("Nueva edad: ")
            print("Persona actualizada con éxito.")
            return
    print("Persona no encontrada.")
