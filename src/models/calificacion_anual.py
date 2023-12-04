from sqlalchemy import Column, Numeric, String, Date, Sequence
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class CalificacionAnual(db.Model):
    __tablename__ = 'calificacion_anual'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    ano_produccion = Column(Date, nullable=False)
    id_calificacion_anual = Column(Numeric(3), nullable=False, default=Sequence('seq_calificacion'))
    puntaje = Column(Numeric(3), nullable=False)
    critico = Column(String(50), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'ano_produccion'], ['produccion_anual_vino.id_pais_pro', 'produccion_anual_vino.id_region', 'produccion_anual_vino.id_bodega', 'produccion_anual_vino.id_vino', 'produccion_anual_vino.ano_produccion'], name='fk_calificacion_produccion'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', 'ano_produccion', 'id_calificacion_anual', name='pk_calificacion_anual'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, id_vino, ano_produccion, puntaje, critico):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.ano_produccion = ano_produccion
        self.puntaje = puntaje
        self.critico = critico