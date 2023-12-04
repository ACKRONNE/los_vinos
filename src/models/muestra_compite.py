from sqlalchemy import Column, Numeric, Integer, Sequence, ForeignKey, Date
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class MuestraCompite(db.Model):
    __tablename__ = 'muestra_compite'
    
    id_concurso = Column(Numeric(3), nullable=False)
    numero_edicion = Column(Numeric(3), nullable=False)
    id_participacion = Column(Numeric(3), nullable=False)
    id_muestra_compite = Column(Numeric(3), nullable=False, default=Sequence('seq_muestracompite'))
    ano_anada = Column(Date, nullable=False)
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), nullable=False)
    posicion_muestra = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_concurso', 'numero_edicion', 'id_participacion'], ['inscripciones.id_concurso', 'inscripciones.numero_edicion', 'inscripciones.id_participacion'], name='fk_muestracompite_inscripcion'),
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega', 'id_vino'], ['vino_marca.id_pais_pro', 'vino_marca.id_region', 'vino_marca.id_bodega', 'vino_marca.id_vino'], name='fk_muestracompite_vino'),
        PrimaryKeyConstraint('id_concurso', 'numero_edicion', 'id_participacion', 'id_muestra_compite', name='pk_muestracompite'),
    )

    def __init__(self, id_concurso, numero_edicion, id_participacion, ano_anada, id_pais_pro, id_region, id_bodega, id_vino, posicion_muestra):
        self.id_concurso = id_concurso
        self.numero_edicion = numero_edicion
        self.id_participacion = id_participacion
        self.ano_anada = ano_anada
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_vino = id_vino
        self.posicion_muestra = posicion_muestra