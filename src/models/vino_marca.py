from sqlalchemy import Column, Numeric, String, Integer, Sequence, ForeignKey, DECIMAL, LargeBinary
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from src.database.db import db

class VinoMarca(db.Model):
    __tablename__ = 'vino_marca'
    
    id_pais_pro = Column(Numeric(3), nullable=False)
    id_region = Column(Numeric(3), nullable=False)
    id_bodega = Column(Numeric(3), nullable=False)
    id_vino = Column(Numeric(3), Sequence('seq_vinos'), nullable=False)
    nombre = Column(String(70), nullable=False)
    meses_maduracion = Column(Numeric(2), nullable=False)
    elaboracion = Column(String(1500), nullable=False)
    maridaje = Column(String(500), nullable=False)
    promedio_años_consumo = Column(Integer, nullable=False)
    temp_servicio = Column(Integer, nullable=False)
    ph = Column(DECIMAL(4,2), nullable=False)
    descripcion_cata = Column(String(1500), nullable=False)
    grado_alcohol = Column(DECIMAL(4,2), nullable=False)
    acidez = Column(DECIMAL(4,2), nullable=False)
    imagen_vino = Column(LargeBinary)
    id_clasificacion = Column(Numeric(3), ForeignKey('clasificaciones.id_clasificacion'), nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['id_pais_pro', 'id_region', 'id_bodega'], ['bodegas.id_pais_pro', 'bodegas.id_region', 'bodegas.id_bodega'], name='fk_vino_bodega'),
        PrimaryKeyConstraint('id_pais_pro', 'id_region', 'id_bodega', 'id_vino', name='pk_vino_marca'),
    )

    def __init__(self, id_pais_pro, id_region, id_bodega, nombre, meses_maduracion, elaboracion, maridaje, promedio_años_consumo, temp_servicio, ph, descripcion_cata, grado_alcohol, acidez, imagen_vino, id_clasificacion):
        self.id_pais_pro = id_pais_pro
        self.id_region = id_region
        self.id_bodega = id_bodega
        self.nombre = nombre
        self.meses_maduracion = meses_maduracion
        self.elaboracion = elaboracion
        self.maridaje = maridaje
        self.promedio_años_consumo = promedio_años_consumo
        self.temp_servicio = temp_servicio
        self.ph = ph
        self.descripcion_cata = descripcion_cata
        self.grado_alcohol = grado_alcohol
        self.acidez = acidez
        self.imagen_vino = imagen_vino
        self.id_clasificacion = id_clasificacion