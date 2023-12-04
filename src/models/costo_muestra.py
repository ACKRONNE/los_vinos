from sqlalchemy import Column, Numeric, Integer, Sequence, ForeignKey, DECIMAL
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class CostoMuestra(db.Model):
    __tablename__ = 'costo_muestra'
    
    id_concurso = Column(Numeric(3), nullable=False)
    numero_edicion = Column(Numeric(3), nullable=False)
    id_costo_muestra = Column(Numeric(3), nullable=False, default=Sequence('seq_costomuestra'))
    numero_muestras = Column(Integer, nullable=False)
    costo = Column(DECIMAL(9,2), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_concurso', 'numero_edicion'], ['edicion.id_concurso', 'edicion.numero_edicion'], name='fk_costo_edicion'),
        PrimaryKeyConstraint('id_concurso', 'numero_edicion', 'id_costo_muestra', name='pk_costomuestra'),
    )

    def __init__(self, id_concurso, numero_edicion, numero_muestras, costo):
        self.id_concurso = id_concurso
        self.numero_edicion = numero_edicion
        self.numero_muestras = numero_muestras
        self.costo = costo