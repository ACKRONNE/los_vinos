-- Insertar Bodega y telefono
CREATE OR REPLACE FUNCTION insert_into_bod_tel(
    id_region numeric(3),
    id_pais_pro numeric(3),
    nombre varchar(50),
    historia varchar(1500),
    enlace_web varchar(50),
    direccion varchar(200),
    fecha_fundacion date,
    resumen_vinos varchar(1500),
    codigo_area numeric[],
    numero numeric[]
    )
RETURNS void AS $$
DECLARE
    _id_bodega numeric(3);
    i integer := 1;
BEGIN
    INSERT INTO bodegas (
        id_pais_pro,
        id_region,
        nombre,
        historia,
        enlace_web,
        direccion,
        fecha_fundacion,
        resumen_vinos
        ) VALUES (
        id_pais_pro,
        id_region,
        nombre,
        historia,
        enlace_web,
        direccion,
        fecha_fundacion,
        resumen_vinos
    ) RETURNING id_bodega INTO _id_bodega;

    -- Insert into the second table using the new_id
    WHILE i <= array_length(codigo_area, 1) LOOP
        INSERT INTO telefonos (
            id_pais_pro,
            id_region,
            id_bodega,
            codigo_area,
            numero
            ) VALUES (
            id_pais_pro,
            id_region,
            _id_bodega,
            codigo_area[i]::numeric,
            numero[i]::numeric
            );
        i := i + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
-- //

CREATE OR REPLACE FUNCTION insert_into_vino_presentacion_variedad(
    id_pais_pro numeric(3),
    id_region numeric(3),
    id_bodega numeric(3),
    nombre varchar(70),
    meses_maduracion numeric(2),
    elaboracion varchar(1500),
    maridaje varchar(500),
    promedio_anos_consumo integer,
    temp_servicio integer,
    ph numeric(4,2),
    descripcion_cata varchar(1500),
    grado_alcohol numeric(4,2),
    acidez numeric(4,2),
    imagen_data bytea,
    id_clasificacion numeric(3),
    tipo varchar[],
    descripcion varchar[],
    cantidad_botellas integer[],
    id_uva text[]
) RETURNS VOID AS $$
DECLARE
    _id_vino numeric(3);
    _id_uva text;
BEGIN
    -- Insertar en vino_marca y obtener la nueva PK
    INSERT INTO vino_marca (
        id_pais_pro,
        id_region,
        id_bodega,
        nombre,
        meses_maduracion,
        elaboracion,
        maridaje,
        promedio_anos_consumo,
        temp_servicio,
        ph,
        descripcion_cata,
        grado_alcohol,
        acidez,
        imagen_vino,
        id_clasificacion
    ) VALUES (
        id_pais_pro,
        id_region,
        id_bodega,
        nombre,
        meses_maduracion,
        elaboracion,
        maridaje,
        promedio_anos_consumo,
        temp_servicio,
        ph,
        descripcion_cata,
        grado_alcohol,
        acidez,
        imagen_data,
        id_clasificacion
    )
    RETURNING id_vino INTO _id_vino;

    -- Insertar en presentacion usando la nueva PK
    FOR i IN 1..array_length(tipo, 1) LOOP
       INSERT INTO presentacion (
        id_pais_pro, 
        id_region, 
        id_bodega, 
        id_vino, 
        tipo, 
        descripcion, 
        cantidad_botellas
        ) VALUES (
            id_pais_pro, 
            id_region, 
            id_bodega, 
            _id_vino, 
            tipo[i], 
            descripcion[i], 
            cantidad_botellas[i]);
    END LOOP;

    -- Insertar en la tabla VariedadVino
    FOREACH _id_uva IN ARRAY id_uva LOOP
    INSERT INTO variedad_vino (
        id_pais_pro, 
        id_region, 
        id_bodega, 
        id_vino, 
        id_uva
        ) VALUES (
            id_pais_pro, 
            id_region, 
            id_bodega, 
            _id_vino, 
            _id_uva::numeric(3)
        );
    END LOOP;

END;
$$ LANGUAGE plpgsql;


-- Insertar Produccion
CREATE OR REPLACE FUNCTION insert_into_produccion(
    id_pais_pro numeric(3),
    id_region numeric(3),
    id_bodega numeric(3),
    id_vino numeric(3),
    ano_produccion date,
    botellas_producidas integer,
    total_dest_exp_hl integer,
    clasificacion_anada varchar(5)
    )
RETURNS void AS $$
BEGIN
    INSERT INTO produccion_anual_vino (
        id_pais_pro,
        id_region,
        id_bodega,
        id_vino,
        ano_produccion,
        botellas_producidas,
        total_dest_exp_hl,
        clasificacion_anada
        ) VALUES (
        id_pais_pro,
        id_region,
        id_bodega,
        id_vino,
        ano_produccion,
        botellas_producidas,
        total_dest_exp_hl,
        clasificacion_anada
    );
END
$$ LANGUAGE plpgsql;
-- //