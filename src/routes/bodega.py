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
        
        # Atributos de bodega
        _nombre =  request.form['bod-nombre']
        _historia = request.form['bod-historia']
        _enlace_web = request.form['bod-enlace_web']
        _direccion = request.form['bod-direccion']
        _fecha_fundacion = request.form['bod-fecha_fundacion']
        _resumen_vinos = request.form['bod-resumen_vinos']
        
        
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
        
        # Atributos de telefono
        _codigo_area = request.form['tlf-codigo_area']
        _numero = request.form['tlf-numero']
        

        return render_template('index.html')
    else:
        return render_template('bodega.html')
# //   
    