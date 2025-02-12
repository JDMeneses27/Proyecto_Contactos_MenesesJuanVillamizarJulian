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
                    opc_C = agregar_contactos()





def agregar_contactos():
    while True:
        print("""
          ╔════════════════════════════════════════════════════════╗
          ║Ingrese los siguientes datos para registrar el contacto:║
          ╚════════════════════════════════════════════════════════╝
              """)
        