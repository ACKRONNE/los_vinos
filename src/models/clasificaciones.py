from sqlalchemy import Column, Numeric, String, Integer, Sequence, ForeignKey
from src.database.db import db

class Clasificaciones(db.Model):
    __tablename__ = 'clasificaciones'
    
    id_clasificacion = Column(Numeric(3), Sequence('seq_clasificacion'), primary_key=True)
    nombre = Column(String(50), nullable=False)
    nivel = Column(Integer, nullable=False)
    descripcion = Column(String(200), nullable=False)
    id_padre_clasificacion = Column(Numeric(3), ForeignKey('clasificaciones.id_clasificacion'))

    def __init__(self, nombre, nivel, descripcion, id_padre_clasificacion=None):
        self.nombre = nombre
        self.nivel = nivel
        self.descripcion = descripcion
        self.id_padre_clasificacion = id_padre_clasificacion