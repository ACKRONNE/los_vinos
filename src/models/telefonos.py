from sqlalchemy import Column, Numeric
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Telefonos(db.Model):
    __tablename__ = 'telefonos'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    codigo_area = Column(Numeric(4), nullable=False)
    numero = Column(Numeric(10), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega'], ['bodegas.id_pais_pro', 'bodegas.id_region', 'bodegas.id_bodega'], name='fk_tlf_bodega'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'codigo_area', 'numero', name='pk_tlf'),
    )
    
    def __init__(self, id_pais_pro, id_region, id_bodega, codigo_area, numero):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.codigo_area = codigo_area
        self.numero = numero