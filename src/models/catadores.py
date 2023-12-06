from sqlalchemy import Column, Numeric, String, Date, CheckConstraint
from src.database.db import db

class Catadores(db.Model):
    __tablename__ = 'catadores'
    
    doc_identidad = Column(Numeric(9), primary_key=True)
    primer_nombre = Column(String(50), nullable=False)
    primer_apellido = Column(String(50), nullable=False)
    segundo_apellido = Column(String(50), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    nivel = Column(String(10), nullable=False)
    segundo_nombre = Column(String(50))
    resumen_curricular = Column(String(1000))
    
    __table_args__ = (
        CheckConstraint(nivel.in_(['aprendiz', 'critico']), name='check_nivel'),
    )

    def __init__(self, doc_identidad, primer_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, nivel, segundo_nombre=None, resumen_curricular=None):
        self.doc_identidad = doc_identidad
        self.primer_nombre = primer_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nivel = nivel
        self.segundo_nombre = segundo_nombre
        self.resumen_curricular = resumen_curricular