from utils import *
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
            case 1:
                agregar_contactos()
            case 2:
                editar_contactos()




    def editar_contactos():
        while True:
            print("""
            ╔════════════════════════════════════════════════════════╗
            ║                     EDITAR CONTACTO:                   ║
            ║════════════════════════════════════════════════════════║   
            ║                 1. Nombre                              ║
            ║                 2. Numero de telefono                  ║
            ║                 3. Salir                               ║
            ╚════════════════════════════════════════════════════════╝  
                            """)
            opc_C = int(input('Selecciona una opción (1-3):'))
            return opc_C

    edit = True
    while edit:
        try:
            match editar_contactos():
                case 1:
                    editName()
                    input("Presiona enter para continuar...")
                case 2:
                    editNumber()
                    input("Presiona enter para continuar...")
                case 3:
                    print("Has salido del programa")
                    edit = False  
                case _:
                    print("Esta opcion no existe")
                    
                            
        except Exception as e:
            print(f"Error: {e}. Selecciona una opción correcta.")
            input("Presiona Enter para continuar...")
                
def agregar_contactos():
    while True:
        print("")
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║Ingrese los siguientes datos para registrar el contacto:║
          ╚════════════════════════════════════════════════════════╝
              """)
        print("")
        
        

