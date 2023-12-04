from sqlalchemy import Column, Numeric, Integer, Sequence, ForeignKey, Date
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Inscripciones(db.Model):
    __tablename__ = 'inscripciones'
    
    id_concurso = Column(Numeric(3), nullable=False)
    numero_edicion = Column(Numeric(3), nullable=False)
    id_participacion = Column(Numeric(3), nullable=False, default=Sequence('seq_inscripcion'))
    fecha_incripcion = Column(Date, nullable=False)
    posicion_catador = Column(Integer)
    doc_catador_aprendiz = Column(Numeric(9))
    id_pais_pro = Column(Numeric(3))
    id_region = Column(Numeric(3))
    id_bodega = Column(Numeric(3))
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega'], ['bodegas.id_pais_pro', 'bodegas.id_region', 'bodegas.id_bodega'], name='fk_inscripcion_bodega'),
        ForeignKeyConstraint(['id_concurso', 'numero_edicion'], ['edicion.id_concurso', 'edicion.numero_edicion'], name='fk_incripcion_edicion'),
        ForeignKeyConstraint(['doc_catador_aprendiz'], ['catadores.doc_identidad'], name='fk_incripcion_catadores'),
        PrimaryKeyConstraint('id_concurso', 'numero_edicion', 'id_participacion', name='pk_incripcion'),
    )

    def __init__(self, id_concurso, numero_edicion, fecha_incripcion, posicion_catador, doc_catador_aprendiz, id_pais_pro, id_region, id_bodega):
        self.id_concurso = id_concurso
        self.numero_edicion = numero_edicion
        self.fecha_incripcion = fecha_incripcion
        self.posicion_catador = posicion_catador
        self.doc_catador_aprendiz = doc_catador_aprendiz
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega