from sqlalchemy import Column, Numeric, ForeignKeyConstraint, PrimaryKeyConstraint
from src.database.db import db

class Planifica(db.Model):
    __tablename__ = 'planifica'
    
    id_organismo = Column(Numeric(3), nullable=False)
    id_concurso = Column(Numeric(3), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_organismo'], ['organismos.id_organismo'], name='fk_planifica_organismo'),
        ForeignKeyConstraint(['id_concurso'], ['concursos.id_concurso'], name='fk_planifica_concurso'),
        PrimaryKeyConstraint('id_organismo', 'id_concurso', name='pk_planifica'),
    )

    def __init__(self, id_organismo, id_concurso):
        self.id_organismo = id_organismo
        self.id_concurso = id_concurso