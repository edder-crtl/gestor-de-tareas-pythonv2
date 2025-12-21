import json, os
from clases import Tarea, ImportanciaTarea, EstadoTarea
from datetime import datetime



def cargar_tareas(archivo="tareas.json"):
    if not os.path.exists(archivo):
        return []
    
    with open(archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)
    
    tareas = []
    for item in datos:
        tarea = Tarea(
            titulo=item["titulo"],
            descripcion=item["descripcion"],
            fecha_creacion=datetime.fromisoformat(item["fecha_creacion"]),
            fecha_entrega=datetime.fromisoformat(item["fecha_entrega"]),
            estado=EstadoTarea(item["estado"]),
            importancia=ImportanciaTarea(item["importancia"])
        )
        tareas.append(tarea)
    
    return tareas

def guardar_tareas(lista):
    lista_dicts = []
    for t in lista:

        d = {
            "titulo": t.titulo,
            "descripcion": t.descripcion,
            "fecha_creacion": t.fecha_creacion.isoformat(),
            "fecha_entrega": t.fecha_entrega.isoformat(),
            "estado": t.estado.value,
            "importancia": t.importancia.value if hasattr(t.importancia, 'value') else t.importancia
        }
        lista_dicts.append(d)

    with open("tareas.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_dicts, archivo, indent=4, ensure_ascii=False)
