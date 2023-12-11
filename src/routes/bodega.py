from flask import Blueprint, render_template, request, flash, jsonify, redirect
from src.database.db import db
from sqlalchemy import select

# FIXME: Pasar estas librerias a catalogo
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
    
    get_pai = PaisesProductores.query.all()
    
    if request.method == "POST":
        
        # Obtencion de la PK del pais
        _nombrePai = request.form['bod-nombrePai']
        _id_pais_pro = select(PaisesProductores.id_pais_pro).where(PaisesProductores.nombre == _nombrePai).scalar_subquery()
        # //
        
        # Obtencion de PK de la region
        _nombreReg = request.form['bod-nombreReg']
        _id_region = select(Regiones.id_region).where(Regiones.nombre == _nombreReg).scalar_subquery()
        # //
        
        # Atributos de bodega
        _nombre =  request.form['bod-nombre']
        _historia = request.form['bod-historia']
        _enlace_web = request.form['bod-enlace_web']
        _direccion = request.form['bod-direccion']
        _fecha_fundacion = request.form['bod-fecha_fundacion']
        _resumen_vinos = request.form['bod-resumen_vinos']
        # //
        
        # Se inserta la bodega en la tabla
        new_bod = Bodegas (
            _id_pais_pro,
            _id_region,
            _nombre,
            _historia,
            _enlace_web,
            _direccion,
            _fecha_fundacion,
            _resumen_vinos
        )

        db.session.add(new_bod)
        db.session.commit()
        db.session.close()
        
        flash("Bodega Agregada con exito")
        # //
        
        # Obtener el id de la bodega recien creada
        _id_bodega = Bodegas.query.filter_by(nombre=_nombre).first().id_bodega 
        # //
        
        # Atributos de telefono
        _codigo_area = request.form['tlf-codigo-area']
        _numero = request.form['tlf-numero']
        # //
        
        # Se inserta el numero en la tabla
        new_telf = Telefonos(
            _id_pais_pro,
            _id_region,
            _id_bodega,
            _codigo_area,
            _numero,
        )

        db.session.add(new_telf)
        db.session.commit()
        db.session.close()
        
        flash("Telefono Agregado con exito")
        # //

        return redirect('index.html')
    else:
        return render_template('bodega.html', get_pai=get_pai)
# //   

# Obtener regiones
@bod.route('/get_regions', methods=['POST'])
def get_regions():
    _nombrePai = request.form.get('bod-nombrePai')
    _id_pais_pro = select(PaisesProductores.id_pais_pro).where(PaisesProductores.nombre == _nombrePai).scalar_subquery()
    
    get_reg = Regiones.query.filter_by(id_pais_pro=_id_pais_pro).all()
    return jsonify([region.nombre for region in get_reg])
# //