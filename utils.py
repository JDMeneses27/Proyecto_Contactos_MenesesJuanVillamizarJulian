import json
from tabulate import tabulate 

def findAll(file_path):
    with open(file_path, "r") as file:
        contactos = json.load(file)
        return contactos

def saveAll(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
                
def editName():
    while(True):
        with open ("data/contactos.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        nameUser = input("Que nombre deseas editar?: ")
        nameEdit = input("Introduce el nuevo nombre: ")
        found = False
        for user in data:
            if user.get('nombre') == nameUser:   
                user['nombre'] = nameEdit
                found = True
        if found:
            with open("data/contactos.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El nombre ha sido actualizado.")
        else:
            print("El nombre no se encontró en los datos.")

def editNumber():
    while(True):
        with open ("data/contactos.json", "r", encoding="utf-8" ) as file:
            data = json.load(file)
        print (tabulate(data, headers='keys', tablefmt='grid'))
        numberUser = int(input("Que telefono deseas editar?: "))
        numberEdit = int(input("Introduce el nuevo telefono: "))
        found = False
        for user in data:
            if user.get('telefono') == numberUser:   
                user['telefono'] = numberEdit
                found = True
        if found:
            with open("data/contactos.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("El telefono ha sido actualizado.")
        else:
            print("El telefono no se encontró en los datos.")

