from flask import Blueprint, render_template, request, flash, send_file, jsonify
from sqlalchemy import select, or_, and_, distinct
from sqlalchemy.orm import aliased
from src.database.db import db


# Librerias para las imagenes
from io import BytesIO
from PIL import Image
# //

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
    
    get_bod = Bodegas.query.all()
    get_tipo1 = Clasificaciones.query.filter(or_(Clasificaciones.nivel == 1, Clasificaciones.id_clasificacion == 140)).all()
    get_pre = db.session.query(distinct(Presentacion.tipo)).all()
    get_pre = [t[0] for t in get_pre]
    get_uva = VitisVinifera.query.all()
    
    if request.method == "POST":
        
        # Nombre de la bodega
        _nombreBod = request.form['cat-nombreBod']
        _id_bodega = select(Bodegas.id_bodega).where(Bodegas.nombre == _nombreBod).scalar_subquery()
        _id_pais_pro = db.session.query(Bodegas.id_pais_pro).filter(Bodegas.id_bodega == _id_bodega)
        _id_region = db.session.query(Bodegas.id_region).filter(Bodegas.id_bodega == _id_bodega)
        # //
        
        # Clasificacion
        _nombreCla2 = request.form['cat-nombreCla2']
        _id_Clasificacion = select(Clasificaciones.id_clasificacion).where(Clasificaciones.nombre == _nombreCla2).scalar_subquery()
        # //
        
        # Captula de datos de vino_marca
        _nombre = request.form['cat-nombre']
        _meses_maduracion = request.form['cat-meses-maduracion']
        _elaboracion = request.form['cat-elaboracion']
        _maridaje = request.form['cat-maridaje']
        _promedio_anos_consumo = request.form['cat-promedio-anos-consumo']
        _temp_servicio = request.form['cat-temp-servicio']
        _ph = request.form['cat-ph']
        _descripcion_cata = request.form['cat-descripcion-cata']
        _grado_alcohol = request.form['cat-grado-alcohol']
        _acidez = request.form['cat-acidez']
        _imagen_vino = request.form['cat-imagen-vino']
        # //
            
        _imagen_data = _imagen_vino.read()
        
        new_vin = VinoMarca(
            _id_pais_pro,
            _id_region,
            _id_bodega,
            _nombre,
            _meses_maduracion,
            _elaboracion,
            _maridaje,
            _promedio_anos_consumo,
            _temp_servicio,
            _ph,
            _descripcion_cata,
            _grado_alcohol,
            _acidez,
            _imagen_data,
            _id_Clasificacion,
        )

        db.session.add(new_vin)
        db.session.commit()
        db.session.close()

        flash("Vino Agregado con exito")
        
        _id_vino = db.session.query(VinoMarca.id_vino).filter(
            and_(
                VinoMarca.id_pais_pro == _id_pais_pro,
                VinoMarca.id_region == _id_region,
                VinoMarca.id_bodega == _id_bodega,
                VinoMarca.nombre == _nombre
            )
        ).first().id_vino
        
        # Captura de datos de presentacion
        _tipo = request.form['cat-tipo']
        _descripcion = request.form['cat-descripcion']
        _cantidad_botellas = request.form['cat-cantidad-botellas']
        # //
        
        # Inserccion de Presentacion
        # FIXME: Un vino puede tener varias presentaciones
        new_pre = Presentacion(
            _id_pais_pro,
            _id_region,
            _id_bodega,
            _id_vino,
            _tipo,
            _descripcion,
            _cantidad_botellas
        )

        db.session.add(new_pre)
        db.session.commit()
        db.session.close()

        flash("Presentacion Agregada con exito")
        # //
        
        # Captura de datos de vitis vinifera
        _nombre_variedad = request.form['cat-nombre-variedad']
        _tipo_uva  = request.form['cat-tipo-uva']
        # //
        
        # Inserccion de Presentacion
        new_uva = VitisVinifera(
            _nombre_variedad,
            _tipo_uva
        )

        db.session.add(new_uva)
        db.session.commit()
        db.session.close()

        flash("Uva Agregada con exito")
        # //
        
        # Obtener el id de la uva
        _id_uva = db.session.query(VitisVinifera.id_uva).filter(
            and_(
                VitisVinifera.nombre_variedad == _nombre_variedad,
                VitisVinifera.tipo_uva == _tipo_uva,
            )
        ).first().id_uva
        # //
        
        # Inserccion de Presentacion
        new_var = VariedadVino(
            _id_pais_pro,
            _id_region,
            _id_bodega,
            _id_vino,
            _id_uva
        )

        db.session.add(new_var)
        db.session.commit()
        db.session.close()

        flash("Variedad Agregada con exito")
        # //
        
        return render_template('index.html')
    else:
        return render_template('catalogo.html', get_bod=get_bod, get_tipo1=get_tipo1, get_pre=get_pre, get_uva=get_uva)
# //   

# FIXME: Falta definir el tamaño de las imagenes
# Guardar imagenes en la BD
@cat.route('/show_image/<int:id_vino>', methods=['GET'])
def showImage(id_vino):
    bodega = VinoMarca.query.get(id_vino)
    
    if bodega is None or bodega.imagen is None:
        return "Imagen no encontrada"
    
    # Crear una imagen PIL a partir de los datos binarios
    imagen = Image.open(BytesIO(bodega.imagen))
    
    # Crear un objeto BytesIO para almacenar la imagen
    img_io = BytesIO()
    
    # Guardar la imagen en el objeto BytesIO en formato JPEG
    imagen.save(img_io, 'JPEG')
    img_io.seek(0)
    
    # Devolver la imagen como respuesta
    return send_file(img_io, mimetype='image/jpeg')
# //

# Obtener las subclasificaciones
@cat.route('/get_clas', methods=['POST'])
def get_clas():
    
    # Crear un alias para la tabla Clasificaciones
    ClasificacionesAlias = aliased(Clasificaciones)
    
    _nombreCla1 = request.form['cat-nombreCla']
    _id_Clasificacion1 = select(Clasificaciones.id_clasificacion).where(Clasificaciones.nombre == _nombreCla1).scalar_subquery()
    
    get_tipo2 = db.session.query(
        Clasificaciones.nombre
    ).join(
        ClasificacionesAlias, 
       _id_Clasificacion1 == Clasificaciones.id_padre_clasificacion
    ).filter(
        and_(ClasificacionesAlias.nombre == _nombreCla1, Clasificaciones.nombre != 'ESPECIALES')
    ).all()
    
    return jsonify([clasificacion.nombre.capitalize() for clasificacion in get_tipo2])
# //