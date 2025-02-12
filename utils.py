import json
import re

def findAll(file_path):
    with open(file_path, "r") as file:
        contactos = json.load(file)
        return contactos

def saveAll(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
                




def validar_nombre(nombre):
    try:
        return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]+$", nombre))
    except ValueError:
        "Error validando el nombre"



def validar_telefono(telefono):
    try:
        if telefono>=1000000000 and telefono <= 9999999999:
            return True
    except ValueError:
        "Error validando el telefono"



def validar_correo(correo):
    try:
        return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ@gmail.com\s]+$", correo))
    except ValueError:
        "Error validando el correo"



def validar_direccion(direccion):
    try:
        return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ1-9\s]+$", direccion))
    except ValueError:
        "Error validando la direccion"

