from sqlalchemy import Column, Numeric, Date
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class Edicion(db.Model):
    __tablename__ = 'edicion'
    id_concurso = Column(Numeric(3), nullable=False)
    numero_edicion = Column(Numeric(3), nullable=False)
    fecha_ini = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    fecha_lim_inscripcion = Column(Date, nullable=False)
    costo_inscripcion = Column(Numeric(9,2), nullable=False)
    fecha_lim_envio_muestra = Column(Date)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_concurso'], ['concursos.id_concurso'], name='fk_edicion_concurso'),
        PrimaryKeyConstraint('id_concurso', 'numero_edicion', name='pk_edicion'),
    )

    def __init__(self, id_concurso, numero_edicion, fecha_ini, fecha_fin, fecha_lim_inscripcion, costo_inscripcion, fecha_lim_envio_muestra):
        self.id_concurso = id_concurso
        self.numero_edicion = numero_edicion
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.fecha_lim_inscripcion = fecha_lim_inscripcion
        self.costo_inscripcion = costo_inscripcion
        self.fecha_lim_envio_muestra = fecha_lim_envio_muestra