from flask import Blueprint, render_template, request, flash, send_file, jsonify, redirect, url_for
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
        _id_Clasificacion = request.form['cat-nombreCla2']
        print(_id_Clasificacion)
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
        _imagen_vino = request.files['cat-imagen-vino']
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

        flash("Vino Agregado con exito")
        
        _id_vino = db.session.query(VinoMarca.id_vino).filter(
            and_(
                VinoMarca.id_pais_pro == _id_pais_pro,
                VinoMarca.id_region == _id_region,
                VinoMarca.id_bodega == _id_bodega,
                VinoMarca.nombre == _nombre
            )
        ).first().id_vino
        
        # PRESENTACION
        # Captura de datos de presentacion
        _tipo = request.form.getlist('cat-tipo[]')
        _descripcion = request.form.getlist('cat-descripcion[]')
        _cantidad_botellas = request.form.getlist('cat-cantidad-botellas[]')
        # //
        
        # Inserccion de Presentacion
        for tipo, descripcion, cantidad in zip(_tipo, _descripcion, _cantidad_botellas,):
            new_pre = Presentacion(
                _id_pais_pro,
                _id_region,
                _id_bodega,
                _id_vino,
                tipo,
                descripcion,
                cantidad
            )
            db.session.add(new_pre)
                    
        flash("Presentacion Agregada con exito")
        # //
        # //
        
        # VARIEDAD VINO
        _id_uva = request.form.getlist('cat-nombre-variedad[]')
        # //

        # Inserccion de Variedad Vino
        for uva in _id_uva:
            new_var = VariedadVino(
                _id_pais_pro,
                _id_region,
                _id_bodega,
                _id_vino,
                uva
            )
            db.session.add(new_var)

        flash("Variedad Agregada con exito")
        # //
        # //
        db.session.commit()
        db.session.close()
        
        return redirect(url_for('index.index'))
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
        Clasificaciones.nombre, Clasificaciones.id_clasificacion
    ).join(
        ClasificacionesAlias, 
       _id_Clasificacion1 == Clasificaciones.id_padre_clasificacion
    ).filter(
        and_(ClasificacionesAlias.nombre == _nombreCla1, Clasificaciones.nombre != 'ESPECIALES')
    ).all()
    
    return jsonify([(clasificacion.nombre.capitalize(), clasificacion.id_clasificacion) for clasificacion in get_tipo2])
# //