from sqlalchemy import Column, Numeric
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class VariedadVino(db.Model):
    __tablename__ = 'variedad_vino'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    id_uva = Column(Numeric(3), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino'], ['vino_marca.id_pais_pro', 'vino_marca.id_region', 'vino_marca.id_bodega', 'vino_marca.id_vino'], name='fk_variedad_vino'),
        ForeignKeyConstraint(['id_uva'], ['vitis_vinifera.id_uva'], name='fk_variedad_uva'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'id_uva', name='pk_variedad'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, id_vino, id_uva):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.id_uva = id_uva