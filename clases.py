from dataclasses import dataclass
import datetime
from enum import Enum


class EstadoTarea(Enum):
    PENDIENTE = 1
    EN_PROGRESO = 2
    COMPLETADA = 3

mapa_estados={
    1: EstadoTarea.PENDIENTE,
    2: EstadoTarea.EN_PROGRESO,
    3: EstadoTarea.COMPLETADA
}



class ImportanciaTarea(Enum):
    BAJA= 1
    MEDIA= 2
    ALTA=3


Mapa_importancia={
    1: ImportanciaTarea.BAJA,
    2: ImportanciaTarea.MEDIA,
    3: ImportanciaTarea.ALTA
}



@dataclass
class Tarea:
    titulo : str
    descripcion:str
    fecha_creacion: datetime.datetime
    fecha_entrega : datetime.datetime
    estado : int ### manejo de diccionario
    importancia : int ### diccionario 
