from sqlalchemy import Column, String, Numeric, ForeignKey, Sequence
from sqlalchemy.schema import PrimaryKeyConstraint
from src.database.db import db

class Regiones(db.Model):
    __tablename__ = 'regiones'
    
    id_pais_pro = Column(Numeric(3), ForeignKey('paises_productores.id_pais_pro'), primary_key=True)
    id_region = Column(Numeric(3), primary_key=True, default=Sequence('seq_region'))
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(500), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id_pais_pro', 'id_region', name='pk_region'),
    )

    def __init__(self, id_pais_pro, nombre, descripcion):
        self.id_pais_pro = id_pais_pro
        self.nombre = nombre
        self.descripcion = descripcion