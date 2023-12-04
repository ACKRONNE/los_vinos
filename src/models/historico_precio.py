from sqlalchemy import Column, Numeric, Date, ForeignKeyConstraint, PrimaryKeyConstraint, DECIMAL
from src.database.db import db

class HistoricoPrecio(db.Model):
    __tablename__ = 'historico_precio'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    id_presentacion = Column(Numeric(3), nullable=False)
    ano_historico = Column(Date, nullable=False)
    precio = Column(DECIMAL(6, 2), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'id_presentacion'], ['presentacion.id_pais_pro', 'presentacion.id_region', 'presentacion.id_bodega', 'presentacion.id_vino', 'presentacion.id_presentacion'], name='fk_historico_presentacion'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'id_presentacion', 'ano_historico', name='pk_historico'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, id_vino, id_presentacion, ano_historico, precio):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.id_presentacion = id_presentacion
        self.ano_historico = ano_historico
        self.precio = precio