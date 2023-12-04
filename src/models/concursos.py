from sqlalchemy import Column, Numeric, String, Sequence, CheckConstraint
from src.database.db import db

class Concursos(db.Model):
    __tablename__ = 'concursos'
    
    id_concurso = Column(Numeric(3), primary_key=True, default=Sequence('seq_concursos'))
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=False)
    tipo_concurso = Column(String(5), nullable=False)
    alcance = Column(String(15), nullable=False)
    tipo_cata = Column(String(20), nullable=False)
    
    __table_args__ = (
        CheckConstraint(tipo_concurso.in_(['cataV', 'cataA']), name='check_tipoconcurso'),
        CheckConstraint(alcance.in_(['nacional', 'internacional']), name='check_alcance'),
        CheckConstraint(tipo_cata.in_(['a ciegas', 'varietal', 'horizontal', 'vertical', 'varietal/vertical']), name='check_tipocata'),
    )

    def __init__(self, nombre, descripcion, tipo_concurso, alcance, tipo_cata):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_concurso = tipo_concurso
        self.alcance = alcance
        self.tipo_cata = tipo_cata