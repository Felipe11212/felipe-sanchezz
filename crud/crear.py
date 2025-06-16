personas=[]
def crearPersona():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    persona = {"id": len(personas)+1, "nombre": nombre, "edad": edad}
    personas.append(persona)
    print("Persona agregada con éxito.")
