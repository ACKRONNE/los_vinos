from sqlalchemy import Column, Numeric, String, ForeignKey
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class DenominacionesOrigen(db.Model):
    __tablename__ = 'denominaciones_origen'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_uva = Column(Numeric(3), ForeignKey('vitis_vinifera.id_uva'), nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(500))

    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region'], ['regiones.id_pais_pro', 'regiones.id_region'], name='fk_DO_region'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_uva', name='pk_DO'),
    )

    def __init__(self, id_pais_pro, id_region, id_uva, nombre, descripcion):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_uva = id_uva
        self.nombre = nombre
        self.descripcion = descripcion