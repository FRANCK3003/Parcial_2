import json
def guardar_archivo_json(ruta:str, dato:any):
    with open(ruta,"w") as archivo:
        json.dump(dato,archivo,indent=4)


def cargar_json(ruta):
    with open(ruta,"r") as archivo:
        datos = json.load(archivo)
    return datos



def cargar_archivo(path,dato):
    lista_score = []
    try:
        lista_score = cargar_json(path)
    except:
        guardar_archivo_json(path,[])
    lista_score.append(dato)
    guardar_archivo_json(path,lista_score)