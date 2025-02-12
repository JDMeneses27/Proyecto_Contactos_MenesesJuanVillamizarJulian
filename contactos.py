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
            case "2":
                while True:
                    editar_contactos()



def editar_contactos():
    while True:
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║                     EDITAR CONTACTO:                   ║
          ║════════════════════════════════════════════════════════║   
          ║                 1. Nombre                              ║
          ║                 2. Numero de telefono                  ║
          ║                 3. Salir                                       ║
          ╚════════════════════════════════════════════════════════╝  
                          """)
        opc = int(input('Selecciona una opción (1-3):'))
        return opc
            
with open ("data/book.json", "r", encoding="utf-8" ) as file:
    data = json.load(file)

def agregar_contactos():
    while True:
        print("")
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║Ingrese los siguientes datos para registrar el contacto:║
          ╚════════════════════════════════════════════════════════╝
              """)
        print("")
        
        



