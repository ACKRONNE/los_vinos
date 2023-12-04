from sqlalchemy import Column, Numeric, String, Integer, Sequence, CheckConstraint
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Presentacion(db.Model):
    __tablename__ = 'presentacion'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    id_presentacion = Column(Numeric(3), nullable=False, default=Sequence('seq_presentacion'))
    tipo = Column(String(10), nullable=False)
    descripcion = Column(String(700))
    cantidad_botellas = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino'], ['vino_marca.id_pais_pro', 'vino_marca.id_region', 'vino_marca.id_bodega', 'vino_marca.id_vino'], name='fk_presentacion_vino'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'id_presentacion', name='pk_presentacion'),
        CheckConstraint(tipo.in_(['botella', 'caja']), name='check_tipopresentacion'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, id_vino, tipo, descripcion=None, cantidad_botellas=None):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.tipo = tipo
        self.descripcion = descripcion
        self.cantidad_botellas = cantidad_botellas