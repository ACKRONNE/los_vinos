from sqlalchemy import Column, Numeric, Date, Integer, String, CheckConstraint
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class ProduccionAnualVino(db.Model):
    __tablename__ = 'produccion_anual_vino'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    ano_produccion = Column(Date, nullable=False)
    botellas_producidas = Column(Integer, nullable=False)
    total_dest_exp_hl = Column(Integer, nullable=False)
    clasificacion_anada = Column(String(5), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino'], ['vino_marca.id_pais_pro', 'vino_marca.id_region', 'vino_marca.id_bodega', 'vino_marca.id_vino'], name='fk_produccion_vino'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'ano_produccion', name='pk_produccion'),
        CheckConstraint(clasificacion_anada.in_(['E', 'MB']), name='check_clasi_anada'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, id_vino, ano_produccion, botellas_producidas, total_dest_exp_hl, clasificacion_anada):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.ano_produccion = ano_produccion
        self.botellas_producidas = botellas_producidas
        self.total_dest_exp_hl = total_dest_exp_hl
        self.clasificacion_anada = clasificacion_anada

