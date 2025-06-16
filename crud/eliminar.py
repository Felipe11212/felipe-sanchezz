

personas=[]

def eliminar():
    id_persona = int(input("ID de la persona a eliminar: "))
    for i, persona in enumerate(personas):
        if persona["id"] == id_persona:
            del personas[i]
            print("Persona eliminada con éxito.")
            return
    print("Persona no encontrada.")
