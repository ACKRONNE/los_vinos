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