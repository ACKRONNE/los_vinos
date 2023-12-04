from sqlalchemy import Column, String, Numeric, Sequence, CheckConstraint
from src.database.db import db

class PaisesImportadores(db.Model):
    __tablename__ = 'paises_importadores'
    
    id_pais_imp = Column(Numeric(3), primary_key=True, default=Sequence('seq_paises_importadores'))
    nombre = Column(String(40), nullable=False, unique=True)
    continente = Column(String(2), nullable=False)
    
    __table_args__ = (
        CheckConstraint("continente IN ('Am', 'Af', 'Eu', 'As', 'Oc')", name='continente_pais_imp'),
    )

    def __init__(self, nombre, continente):
        self.nombre = nombre
        self.continente = continente