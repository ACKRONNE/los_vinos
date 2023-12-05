from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file
from src.database.db import db
from io import BytesIO
from PIL import Image

# Entidades
from src.models.bodegas import Bodegas
from src.models.regiones import Regiones
from src.models.paises_productores import PaisesProductores
from src.models.telefonos import Telefonos
# //

bod = Blueprint('bodega', __name__)


# Agregar Bodega
@bod.route('/add_bodega', methods=['GET','POST'])
def addBodega():
    
    if request.method == "POST":
        
        _nombrePai = request.form['bod-nombrePai']
        
        _nombreReg = request.form['bod-nombreReg']
        
        
        _nombre = 
        _historia = 
        _enlace_web = 
        _direccion = 
        _fecha_fundacion = 
        _resumen_vinos = 
        
        _nombre = request.form['bod-nombre']
        _historia = request.form['bod-historia']
        _direccion_web = request.form['bod-direccion_web']
        _id_region = request.form['bod-id_region'] 
        _imagen = request.files['bod-imagen']
        
        _codigo_area = request.form['tlf-codigo_area']
        _numero = request.form['tlf-numero']
        
        _imagen_data = _imagen.read()
        
        new_bod = Bodegas(
            _nombre,
            _historia,
            _direccion_web,
            _id_region,
            _imagen_data
        )

        db.session.add(new_bod)
        db.session.commit()
        db.session.close()

        flash("Bodega Agregada con exito")

        return render_template('index.html')
    else:
        return render_template('bodega.html')
# //   
    
    
# FIXME: Falta definir el tamaño de las imagenes
# Guardar imagenes en la BD
@bod.route('/show_image/<int:bodega_id>', methods=['GET'])
def showImage(bodega_id):
    bodega = Bodegas.query.get(bodega_id)
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
