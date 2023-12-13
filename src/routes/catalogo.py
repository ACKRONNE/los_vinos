from flask import Blueprint, render_template, request, send_file, jsonify, redirect, url_for
from sqlalchemy import select, or_, and_, distinct, text
from sqlalchemy.orm import Session
from sqlalchemy.orm import aliased
from src.database.db import db


# Entidades
from src.models.bodegas import Bodegas
from src.models.vino_marca import VinoMarca
from src.models.presentacion import Presentacion
from src.models.variedad_vino import VariedadVino
from src.models.vitis_vinifera import VitisVinifera
from src.models.clasificaciones import Clasificaciones
# //

cat = Blueprint('catalogo', __name__)


# Agregar Bodega
@cat.route('/add_catalogo', methods=['GET','POST'])
def addCatalogo():
    
    session = Session(bind=db.engine)
    
    get_bod = Bodegas.query.all()
        
    get_tipo1 = Clasificaciones.query.filter(or_(Clasificaciones.nivel == 1, Clasificaciones.id_clasificacion == 140)).all()
    get_pre = db.session.query(distinct(Presentacion.tipo)).all()
    get_pre = [t[0] for t in get_pre]
    get_uva = VitisVinifera.query.all()
    
    if request.method == "POST":
        
        
        try:
            # Comenzar una nueva transaccion
            session.begin()
            
            # Captura de datos general
            _nombreBod = request.form['cat-nombreBod']
            _id_bodega = db.session.query(Bodegas.id_bodega).filter(Bodegas.nombre == _nombreBod).scalar()
            _id_pais_pro = db.session.query(Bodegas.id_pais_pro).filter(Bodegas.id_bodega == _id_bodega).scalar()
            _id_region = db.session.query(Bodegas.id_region).filter(Bodegas.id_bodega == _id_bodega).scalar()
            
            # Clasificacion
            _id_Clasificacion = int(request.form.get('cat-nombreCla2'))
        
            # Captura de datos de vino_marca
            _nombre = request.form['cat-nombre']
            _meses_maduracion = int(request.form['cat-meses-maduracion'])
            _elaboracion = request.form['cat-elaboracion']
            _maridaje = request.form['cat-maridaje']
            _promedio_anos_consumo = int(request.form['cat-promedio-anos-consumo'])
            _temp_servicio = int(request.form['cat-temp-servicio'])
            _ph = float(request.form['cat-ph'])
            _descripcion_cata = request.form['cat-descripcion-cata']
            _grado_alcohol = float(request.form['cat-grado-alcohol'])
            _acidez = float(request.form['cat-acidez'])
            _imagen_vino = request.files['cat-imagen-vino']
                    
            _imagen_data = _imagen_vino.read()
        
            # Captura de datos de Presentacion
            _tipo = request.form.getlist('cat-tipo[]')
            _descripcion = request.form.getlist('cat-descripcion[]')
            _cantidad_botellas = list(map(int, request.form.getlist('cat-cantidad-botellas[]')))
            
            # Captura de datos de Variedad
            _id_uva = request.form.getlist('cat-nombre-variedad[]')

            session.execute(text("SELECT insert_into_vino_presentacion_variedad(:id_pais_pro, :id_region, :id_bodega, :nombre, :meses_maduracion, :elaboracion, :maridaje, :promedio_anos_consumo, :temp_servicio, :ph, :descripcion_cata, :grado_alcohol, :acidez, :imagen_data, :id_clasificacion, :tipo, :descripcion, :cantidad_botellas, :id_uva)"), 
            {
                "id_pais_pro": _id_pais_pro,
                "id_region": _id_region,
                "id_bodega": _id_bodega,
                "nombre": _nombre,
                "meses_maduracion": _meses_maduracion,
                "elaboracion": _elaboracion,
                "maridaje": _maridaje,
                "promedio_anos_consumo": _promedio_anos_consumo,
                "temp_servicio": _temp_servicio,
                "ph": _ph,
                "descripcion_cata": _descripcion_cata,
                "grado_alcohol": _grado_alcohol,
                "acidez": _acidez,
                "imagen_data": _imagen_data,
                "id_clasificacion": _id_Clasificacion,
                "tipo": _tipo,
                "descripcion": _descripcion,
                "cantidad_botellas": _cantidad_botellas,
                "id_uva": _id_uva
            })
            # //
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
        
        return redirect(url_for('index.index'))
    else:
        return render_template('catalogo.html', get_bod=get_bod, get_tipo1=get_tipo1, get_pre=get_pre, get_uva=get_uva)
# //   

# Obtener las subclasificaciones
@cat.route('/get_clas', methods=['POST'])
def get_clas():
    
    # Crear un alias para la tabla Clasificaciones
    ClasificacionesAlias = aliased(Clasificaciones)
    
    _nombreCla1 = request.form['cat-nombreCla']
    _id_Clasificacion1 = select(Clasificaciones.id_clasificacion).where(Clasificaciones.nombre == _nombreCla1).scalar_subquery()
    
    get_tipo2 = db.session.query(
        Clasificaciones.nombre, Clasificaciones.id_clasificacion
    ).join(
        ClasificacionesAlias, 
       _id_Clasificacion1 == Clasificaciones.id_padre_clasificacion
    ).filter(
        and_(ClasificacionesAlias.nombre == _nombreCla1, Clasificaciones.nombre != 'ESPECIALES')
    ).all()
    
    return jsonify([(clasificacion.nombre.capitalize(), clasificacion.id_clasificacion) for clasificacion in get_tipo2])
# //