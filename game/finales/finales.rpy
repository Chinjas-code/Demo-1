##### FINALES DEL JUEGO #####
#### Aqui van TODOS los finales. Cada final es un "label" y se llega a el con:  jump nombre_del_label
#### Si un final se hace muy largo se puede mover a su propio archivo dentro de esta carpeta (finales/final_2.rpy)
#### y dejar aqui solo la fila del indice.
####
#### ------------------------------ INDICE DE FINALES ------------------------------
####
####  #  | Nombre           | Label                 | Se llega desde                                  | Estado
####  1  | Asimilación      | final_1_asimilacion   | ruta_b2_c (cap1_ruta_b_dejar.rpy)               | Texto listo. Faltan imagen, efectos, sonido
####     |                  |                       | ruta_c2_b (cap1_ruta_c_tirar.rpy)               | y la mecanica de reinicio.
####  2  | (por definir)    |                       |                                                 | Pendiente
####  3  | (por definir)    |                       |                                                 | Pendiente
####
#### (Actualizar esta tabla cada que se agregue o se conecte un final.)
####
#### ------------------------ PLANTILLA PARA UN FINAL NUEVO -------------------------
#### Copiar el bloque de abajo, quitarle los "#" y cambiar el numero / nombre:
####
#### # ============================================================
#### # FINAL 2 - NOMBRE DEL FINAL
#### # ============================================================
#### # Se llega desde: (que ruta / condicion)
####
#### label final_2_nombre:
####
####     # TODO IMAGE:
####     # TODO EFFECT:
####     # TODO SFX:
####
####     "Texto del final."
####
####     return
####
#### ---------------------------------------------------------------------------------


# ============================================================
# FINAL 1 - ASIMILACIÓN
# Se llega desde: ruta_b2_c y ruta_c2_b
# ============================================================

label final_1_asimilacion:

    # TODO IMAGE: INFECTADO 1 ocupando toda la pantalla
    # TODO EFFECT: interfaz oculta
    # TODO EFFECT: zoom lento
    # TODO SFX: ambiente distorsionado

    "Parece mirar al jugador."



    # TODO EFFECT: zoom lento
    # TODO EFFECT: distorsión progresiva
    # TODO SFX: voces repetidas


    #AQUI ESTA ESTO DEL FINAL NO SE COMO HACERLO PERO YA ME DARE UN TIRO JUNTO AL PROGRAMADOR DE DARLE SENTIDO A ESTO



    # ========================================================
    # MECÁNICA ESPECIAL DEL FINAL
    # ========================================================

    # TODO:
    # Al cerrar y volver a abrir el juego, no se debe llegar al menu si no a la misma imagen y que salga un boton que diga reinicio despues de unos segundos
    # Al reiniciarlo debe estar el juego como si anda y todo nuevo
    # TODO:
    # (para esto se puede guardar una bandera en `persistent`, por ejemplo persistent.final_1 = True, y revisarla al iniciar el juego)

    # Hasta que no se ponga ese boton, la escena deberá permanecer activa.

    while True:
        pause
