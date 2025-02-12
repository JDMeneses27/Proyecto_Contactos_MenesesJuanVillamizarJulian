from utils import validar_nombre, validar_telefono, validar_correo, validar_direccion, findAll, saveAll

file_path = "./data/contactos.json"


def menu_principal():
    while True:
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║              BIENVENIDO AL MENÚ PRINCIPAL              ║
          ║════════════════════════════════════════════════════════║
          ║             Sistema de Gestión de Contactos            ║
          ║   1. Agregar Contactos                                 ║
          ║   2. Editar Contacto                                   ║
          ║   3. Eliminar Contacto                                 ║
          ║   4. Buscar Contacto                                   ║
          ║   5. Listar Contactos                                  ║
          ║   6. Salir                                             ║
          ║                                                        ║
          ╚════════════════════════════════════════════════════════╝
              """)
        opc = input("Ingrese una opción (o 'q' para salir): ")
        if opc.lower() == 'q':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        match opc:
            case "1":
                while True:
                    agregar_contactos()
            case "3":
                while True:
                    nombre = get_nombre()
                    eliminar_contactos(file_path, nombre)
            





def agregar_contactos():
    while True:
        print("")
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║Ingrese los siguientes datos para registrar el contacto:║
          ╚════════════════════════════════════════════════════════╝
              """)
        print("")
        nombre = get_nombre()
        telefono = get_telefono()
        correo = get_correo()
        direccion = get_direccion()

        contacto = {
            "nombre":nombre,
            "telefono":telefono,
            "correo":correo,
            "direccion":direccion
        }

        contactos = findAll(file_path)
        contactos.append(contacto)
        saveAll(contactos, file_path)

        

def get_nombre():
    try:
        while True:
            nombre = input("""
                           ║Ingrese el nombre del contacto: ║
                           """)
            if validar_nombre(nombre) == True:
                return nombre
    except ValueError:
        "Error consiguiendo el nombre"

def get_telefono():
    try:
        while True:
            telefono = int(input("""
                            ║Ingrese el numero telefonico del contacto: ║
                                 """))
            if validar_telefono(telefono) == True:
                return telefono
    except ValueError:
        "Error consiguiendo el telefono"

def get_correo():
    try:
        while True:
            correo = input("""
                           ║Ingrese el correo del contacto: ║
                           """)
            if validar_correo(correo) == True:
                return correo
    except ValueError:
        "Error consiguiendo el correo"


def get_direccion():
    try:
        while True:
            direccion = input("""
                            ║Ingrese la direccion del contacto: ║
                              """)
            if validar_direccion(direccion) == True:
                return direccion
    except ValueError:
        "Error consiguiendo el direccion"


def eliminar_contactos(file_path, nombre):
    try:
        contactos = findAll(file_path)
        contador_inicial = len(contactos)
        contactos = [contacto for contacto in contactos if contacto["nombre"] != nombre]
        if len(contactos) == contador_inicial:
            print("No se encontró el contacto a eliminar")
            return False
        saveAll(contactos, file_path)
        print(f"Contacto {nombre} eliminado")
        return True
    except ValueError:
        print("ERROR AL ELIMINAR EL CONTACTO")

