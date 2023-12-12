from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from src.database.db import db
from sqlalchemy import select
from datetime import datetime

# Entidades
from src.models.bodegas import Bodegas
from src.models.vino_marca import VinoMarca
from src.models.produccion_anual_vino import ProduccionAnualVino
# //

ana = Blueprint('anada', __name__)

# Agregar Bodega
@ana.route('/add_anada', methods=['GET','POST'])
def addAnada():
    
    get_vin = VinoMarca.query.all()
    bodega_name = '-'
    
    if request.method == "POST":
        
        _id_vino = request.form['ana-id-vino']
        _id_pais_pro = select(VinoMarca.id_pais_pro).where(VinoMarca.id_vino == _id_vino).scalar_subquery()
        _id_region = select(VinoMarca.id_region).where(VinoMarca.id_vino == _id_vino).scalar_subquery()
        _id_bodega = select(VinoMarca.id_bodega).where(VinoMarca.id_vino == _id_vino).scalar_subquery()
        
        bodega_name = db.session.execute(select(Bodegas.nombre).where(Bodegas.id_bodega == _id_bodega)).scalar_one_or_none()
        
        _ano_produccion = (request.form['ana-ano-produccion'] + "-01-01")
        _botellas_producidas = request.form['ana-botellas-producidas']
        _total_dest_exp_hl = request.form['ana-total-dest-exp-hl']
        _clasificacion_anada = request.form['ana-clasificacion-anada']
        
        
        # Se inserta la bodega en la tabla
        new_pro = ProduccionAnualVino (
            _id_pais_pro,
            _id_region,
            _id_bodega,
            _id_vino,
            _ano_produccion,
            _botellas_producidas,
            _total_dest_exp_hl,
            _clasificacion_anada
        )

        db.session.add(new_pro)
        db.session.commit()
        db.session.close()
        
        flash("Produccion Agregada con exito")
        # //
        
        return redirect(url_for('index.index'))
    else:
        return render_template('anada.html', get_vin=get_vin, bodega_name=bodega_name)
# //   

@ana.route('/get_bodega_name', methods=['POST'])
def get_bodega_name():
    _id_vino = request.form['ana-id-vino']
    _id_bodega = select(VinoMarca.id_bodega).where(VinoMarca.id_vino == _id_vino).scalar_subquery()
    
    bodega_name = db.session.execute(select(Bodegas.nombre).where(Bodegas.id_bodega == _id_bodega)).scalar()
    return jsonify(bodega_name=bodega_name)