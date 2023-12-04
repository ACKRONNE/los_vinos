from sqlalchemy import Column, String, Numeric, CheckConstraint, Sequence
from src.database.db import db

class PaisesProductores(db.Model):
    __tablename__ = 'paises_productores'
    
    id_pais_pro = Column(Numeric(3), primary_key=True, default=Sequence('seq_paispro'))
    nombre = Column(String(40), unique=True, nullable=False)
    continente = Column(String(2), nullable=False)
    descripcion_productor = Column(String(1500), nullable=False)
    hectareas_cultivadas = Column(Numeric(8,2), nullable=False)
    moneda = Column(String(7), nullable=False)
    
    
    __table_args__ = (
        CheckConstraint(continente.in_(['Am', 'Af', 'Eu', 'As', 'Oc']), name='continente_pais_pro'),
        CheckConstraint(moneda.in_(['euros', 'dolares']), name='moneda_pais_pro'),
    )

    def __init__(self, nombre, continente ,descripcion_productor ,hectareas_cultivadas ,moneda):
        self.nombre = nombre
        self.continente = continente
        self.descripcion_productor = descripcion_productor
        self.hectareas_cultivadas = hectareas_cultivadas
        self.moneda = moneda