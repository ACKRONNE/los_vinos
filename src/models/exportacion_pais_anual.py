from sqlalchemy import Column, Numeric, Date, ForeignKey
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from src.database.db import db

class ExportacionPaisAnual(db.Model):
    __tablename__ = 'exportacion_pais_anual'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_pais_imp = Column(Numeric(3), ForeignKey('paises_importadores.id_pais_imp'), nullable=False)
    ano_exportacion = Column(Date, nullable=False)
    vol_hl = Column(Numeric(4), nullable=False)
    
    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega'], ['bodegas.id_pais_pro', 'bodegas.id_region','bodegas.id_bodega'], name='fk_exp_bodega'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_pais_imp', 'ano_exportacion', name='pk_exportacion_pais_anual'),
    )

    bodega = relationship('Bodegas', foreign_keys=[id_pais_pro, id_region, id_bodega])
    pais_importador = relationship('PaisesImportadores', foreign_keys=[id_pais_imp])

    def __init__(self, id_pais_pro, id_region, id_bodega, id_pais_imp, ano_exportacion, vol_hl):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.id_pais_imp = id_pais_imp
        self.ano_exportacion = ano_exportacion
        self.vol_hl = vol_hl