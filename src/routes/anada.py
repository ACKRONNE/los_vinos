from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from sqlalchemy.orm import Session
from src.database.db import db
from sqlalchemy import select, text

# Entidades
from src.models.bodegas import Bodegas
from src.models.vino_marca import VinoMarca

# //

ana = Blueprint('anada', __name__)

# Agregar Bodega
@ana.route('/add_anada', methods=['GET','POST'])
def addAnada():
    
    session = Session(bind=db.engine)
    
    get_vin = VinoMarca.query.all()
    bodega_name = '-'
    
    if request.method == "POST":
        
        try:   
            # Comenzar una nueva transaccion
            session.begin()
            
            _id_vino = request.form['ana-id-vino']
            _id_pais_pro = session.execute(select(VinoMarca.id_pais_pro).where(VinoMarca.id_vino == _id_vino)).scalar()
            _id_region = session.execute(select(VinoMarca.id_region).where(VinoMarca.id_vino == _id_vino)).scalar()
            _id_bodega = session.execute(select(VinoMarca.id_bodega).where(VinoMarca.id_vino == _id_vino)).scalar()

            bodega_name = session.execute(select(Bodegas.nombre).where(Bodegas.id_bodega == _id_bodega)).scalar()

            
            _ano_produccion = (request.form['ana-ano-produccion'] + "-01-01")
            _botellas_producidas = request.form['ana-botellas-producidas']
            _total_dest_exp_hl = request.form['ana-total-dest-exp-hl']
            _clasificacion_anada = request.form['ana-clasificacion-anada']
            
            
            session.execute(text("SELECT insert_into_produccion(:id_pais_pro, :id_region, :id_bodega, :id_vino, :ano_produccion, :botellas_producidas, :total_dest_exp_hl, :clasificacion_anada)"), 
            {
                'id_pais_pro': _id_pais_pro,
                'id_region': _id_region,
                'id_bodega': _id_bodega,
                'id_vino': _id_vino,
                'ano_produccion': _ano_produccion,
                'botellas_producidas': _botellas_producidas,
                'total_dest_exp_hl': _total_dest_exp_hl,
                'clasificacion_anada': _clasificacion_anada
            })
            
            session.commit()    
        except:
            session.rollback()
            raise
        finally:
            session.close()

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