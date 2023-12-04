from sqlalchemy import Column, Numeric, String, Sequence, CheckConstraint
from src.database.db import db

class VitisVinifera(db.Model):
    __tablename__ = 'vitis_vinifera'
    
    id_uva = Column(Numeric(3), Sequence('seq_vitis_vinifera'), primary_key=True)
    nombre_variedad = Column(String(50), nullable=False)
    tipo_uva = Column(String(10), nullable=False)
    
    __table_args__ = (
        CheckConstraint(tipo_uva.in_(['blanca', 'tinta']), name='check_tipouva'),
    )

    def __init__(self, nombre_variedad, tipo_uva):
        self.nombre_variedad = nombre_variedad
        self.tipo_uva = tipo_uva