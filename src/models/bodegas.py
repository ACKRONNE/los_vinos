from sqlalchemy import Column, String, Numeric, Sequence, Date
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Bodegas(db.Model):
    __tablename__ = 'bodegas'
    
    id_pais_pro = Column(Numeric(3), primary_key=True)
    id_region = Column(Numeric(3), primary_key=True)
    id_bodega = Column(Numeric(3), primary_key=True, default=Sequence('seq_bodega'))
    nombre = Column(String(50), nullable=False, unique=True)
    historia = Column(String(1500), nullable=False)
    enlace_web = Column(String(50), nullable=False, unique=True)
    direccion = Column(String(200), nullable=False, unique=True)
    fecha_fundacion = Column(Date, nullable=False)
    resumen_vinos = Column(String(1500), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region'], ['regiones.id_pais_pro', 'regiones.id_region'], name='fk_bodega_region'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', name='pk_bodega'),
    )

    def __init__(self, id_pais_pro, id_region, nombre, historia, enlace_web, direccion, fecha_fundacion, resumen_vinos):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.nombre = nombre
        self.historia = historia
        self.enlace_web = enlace_web
        self.direccion = direccion
        self.fecha_fundacion = fecha_fundacion
        self.resumen_vinos = resumen_vinos