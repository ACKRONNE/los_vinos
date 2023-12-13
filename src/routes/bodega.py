from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from src.database.db import db

# Entidades
from src.models.regiones import Regiones
from src.models.paises_productores import PaisesProductores
# //

bod = Blueprint('bodega', __name__)

# FIXME: Falta arreglar los estilos de telefono

# Agregar Bodega
@bod.route('/add_bodega', methods=['GET','POST'])
def addBodega():

    session = Session(bind=db.engine)
    
    get_pai = PaisesProductores.query.all()
    
    if request.method == "POST":
        
        try:
            # Comenzar una nueva transaccion
            session.begin()
        
            # Obtencion de la PK del pais
            _nombrePai = request.form['bod-nombrePai']
            _id_pais_pro = db.session.execute(select(PaisesProductores.id_pais_pro).where(PaisesProductores.nombre == _nombrePai)).scalar_one()

            # Obtencion de PK de la region
            _nombreReg = request.form['bod-nombreReg']
            _id_region = db.session.execute(select(Regiones.id_region).where(Regiones.nombre == _nombreReg)).scalar_one()
            
            # Atributos de bodega
            _nombre =  request.form['bod-nombre']
            _historia = request.form['bod-historia']
            _enlace_web = request.form['bod-enlace_web']
            _direccion = request.form['bod-direccion']
            _fecha_fundacion = request.form['bod-fecha_fundacion']
            _resumen_vinos = request.form['bod-resumen_vinos']
            # //
                    
            # Atributos de telefono
            _codigo_area = list(map(int, request.form.getlist('tlf-codigo-area[]')))
            _numero = list(map(int, request.form.getlist('tlf-numero[]')))
            
            session.execute(text("SELECT insert_into_bod_tel(:id_region, :id_pais_pro, :nombre, :historia, :enlace_web, :direccion, :fecha_fundacion, :resumen_vinos, :codigo_area, :numero)"), 
                {"id_region": _id_region, 
                 "id_pais_pro": _id_pais_pro, 
                 "nombre": _nombre, 
                 "historia": _historia, 
                 "enlace_web": _enlace_web, 
                 "direccion": _direccion, 
                 "fecha_fundacion": _fecha_fundacion, 
                 "resumen_vinos": _resumen_vinos, 
                 "codigo_area": _codigo_area, 
                 "numero": _numero})
            # //
            
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return redirect(url_for('index.index'))
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