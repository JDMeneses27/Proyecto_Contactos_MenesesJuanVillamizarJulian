import json

def findAll(file_path):
    with open(file_path, "r") as file:
        contactos = json.load(file)
        return contactos

def saveAll(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
                