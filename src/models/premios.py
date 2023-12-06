from sqlalchemy import Column, Numeric, String, Sequence, CheckConstraint, ForeignKey, Integer, DECIMAL
from sqlalchemy.schema import PrimaryKeyConstraint
from src.database.db import db

class Premios(db.Model):
    __tablename__ = 'premios'
    
    id_concurso = Column(Numeric(3), ForeignKey('concursos.id_concurso'), nullable=False)
    id_premio = Column(Numeric(3), default=Sequence('seq_premios'))
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(1000), nullable=False)
    tipo_premio = Column(String(15), nullable=False)
    posicion = Column(Integer, nullable=False)
    premio_monetario = Column(DECIMAL(9, 2))
    
    __table_args__ = (
        PrimaryKeyConstraint('id_concurso', 'id_premio', name='pk_presentacion'),
        CheckConstraint(tipo_premio.in_(['medalla', 'certificado', 'otro']), name='check_tipopremio'),
    )

    def __init__(self, id_concurso, nombre, descripcion, tipo_premio, posicion, premio_monetario=None):
        self.id_concurso = id_concurso
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_premio = tipo_premio
        self.posicion = posicion
        self.premio_monetario = premio_monetario
        
