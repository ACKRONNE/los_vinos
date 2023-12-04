from sqlalchemy import Column, Numeric, ForeignKey
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Jueces(db.Model):
    __tablename__ = 'jueces'
    
    id_concurso = Column(Numeric(3), nullable=False)
    numero_edicion = Column(Numeric(3), nullable=False)
    doc_catador_critico = Column(Numeric(9), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_concurso', 'numero_edicion'], ['edicion.id_concurso', 'edicion.numero_edicion'], name='fk_jueces_edicion'),
        ForeignKeyConstraint(['doc_catador_critico'], ['catadores.doc_identidad'], name='fk_jueces_catadores'),
        PrimaryKeyConstraint('id_concurso', 'numero_edicion', 'doc_catador_critico', name='pk_jueces'),
    )

    def __init__(self, id_concurso, numero_edicion, doc_catador_critico):
        self.id_concurso = id_concurso
        self.numero_edicion = numero_edicion
        self.doc_catador_critico = doc_catador_critico