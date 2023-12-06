from flask import Flask
from src.database.db import db

# Entidades de la BD
# from src.models.bodegas import Bodegas
# from src.models.calificacion_anual import CalificacionAnual
# from src.models.catadores import Catadores
# from src.models.clasificaciones import Clasificaciones
# from src.models.concursos import Concursos
# from src.models.costo_muestra import CostoMuestra
# from src.models.denominaciones_origen import DenominacionesOrigen
# from src.models.edicion import Edicion
# from src.models.exportacion_pais_anual import ExportacionPaisAnual
# from src.models.historico_precio import HistoricoPrecio
# from src.models.inscripciones import Inscripciones
# from src.models.jueces import Jueces
# from src.models.muestra_compite import MuestraCompite
# from src.models.organismos import Organismos
# from src.models.paises_importadores import PaisesImportadores
# from src.models.paises_productores import PaisesProductores
# from src.models.planifica import Planifica
# from src.models.premios import Premios
# from src.models.presentacion import Presentacion
# from src.models.produccion_anual_vino import ProduccionAnualVino
# from src.models.regiones import Regiones
# from src.models.telefonos import Telefonos
# from src.models.variedad_vino import VariedadVino
# from src.models.vino_marca import VinoMarca
# from src.models.vitis_vinifera import VitisVinifera
# //

# Objetos de las rutas
from src.routes.index import ind
from src.routes.bodega import bod

# Librerias para el funcionamiento
from dotenv import load_dotenv
import os
# //

load_dotenv()

app = Flask(__name__)

# Settings de la DB
key = os.environ['SECRETKEY']
config = os.environ['MYSQLCONFIG']

app.secret_key = key
app.config['SQLALCHEMY_DATABASE_URI'] = config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# //

# inicializar la aplicacion con la base de datos
db.init_app(app)
# //
app.register_blueprint(ind)
app.register_blueprint(bod)

