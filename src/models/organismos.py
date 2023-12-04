from sqlalchemy import Column, Numeric, String, Sequence, ForeignKey
from src.database.db import db

class Organismos(db.Model):
    __tablename__ = 'organismos'
    id_organismo = Column(Numeric(3), primary_key=True, default=Sequence('seq_organismo'))
    nombre = Column(String(70), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=False)
    id_pais_pro = Column(Numeric(3), ForeignKey('paises_productores.id_pais_pro'), nullable=False)

    def __init__(self, nombre, descripcion, id_pais_pro):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_pais_pro = id_pais_pro