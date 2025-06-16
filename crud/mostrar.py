
personas=[]
def Mostrar():
    print("\npersonas:")
    for persona in personas:
        print(f"ID: {persona['id']}, Nombre: {persona['nombre']}, Edad: {persona['edad']}")