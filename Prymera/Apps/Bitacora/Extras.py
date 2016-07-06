Bases Dato:


--VISTA PARA LAS OPCIONES DE LA BITACORA

CREATE OR REPLACE VIEW bitacora_opciones AS 
 SELECT "Bitacora_opcion".id,
    (((((((( SELECT "Bitacora_categoria"."NOMBRE"
           FROM "Bitacora_categoria"
          WHERE "Bitacora_categoria".id = "Bitacora_opcion"."CATEGORIA_id"))::text) || ' / '::text) || ((( SELECT "Bitacora_detalle_scategoria"."NOMBRE"
           FROM "Bitacora_detalle_scategoria"
          WHERE "Bitacora_detalle_scategoria".id = "Bitacora_opcion"."DETALLE_SCATEGORIA_id"))::text)) || ' / '::text) || ((( SELECT "Bitacora_herramienta"."NOMBRE"
           FROM "Bitacora_herramienta"
          WHERE "Bitacora_herramienta".id = "Bitacora_opcion"."HERRAMIENTA_id"))::text)) || ' / '::text) || ((( SELECT "Bitacora_sub_categoria"."NOMBRE"
           FROM "Bitacora_sub_categoria"
          WHERE "Bitacora_sub_categoria".id = "Bitacora_opcion"."SUB_CATEGORIA_id"))::text) AS "Detalle"
   FROM "Bitacora_opcion";

ALTER TABLE bitacora_opciones
  OWNER TO prymera;



--VISTA PARA LAS OPCIONES DEL BITACORA DE CAIDAS

CREATE OR REPLACE VIEW bitacora_opciones_comunicacion AS 
 SELECT "Bitacora_opcion_comunicacion".id,
    (((((( SELECT "Bitacora_categoria"."NOMBRE"
           FROM "Bitacora_categoria"
          WHERE "Bitacora_categoria".id = "Bitacora_opcion_comunicacion"."CATEGORIA_id"))::text) || ' / '::text) || ((( SELECT "Bitacora_evento"."NOMBRE"
           FROM "Bitacora_evento"
          WHERE "Bitacora_evento".id = "Bitacora_opcion_comunicacion"."TIPO_EVENTO_id"))::text)) || ' / '::text) || ((( SELECT "Bitacora_factor"."NOMBRE"
           FROM "Bitacora_factor"
          WHERE "Bitacora_factor".id = "Bitacora_opcion_comunicacion"."FACTOR_id"))::text) AS "Detalle"
   FROM "Bitacora_opcion_comunicacion";

ALTER TABLE bitacora_opciones_comunicacion
  OWNER TO prymera;