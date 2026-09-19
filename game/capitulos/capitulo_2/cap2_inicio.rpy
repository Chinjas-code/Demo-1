##### CAPITULO 2 - INICIO #####
#### Aqui se escribe el capitulo 2 de la demo.
#### Se llega desde el final de las rutas del capitulo 1 (A, B1, B2-A, B2-B, C1, C2-A) con "jump capitulo_2".
#### Si el capitulo 2 se hace largo, crear mas archivos en esta misma carpeta (ej. cap2_ruta_a.rpy, cap2_ruta_b.rpy)
#### y conectarlos con jump igual que en capitulo_1.
#### Los sprites del MC se muestran con: show mc <expresion>  (ver recursos.rpy). Fondos nuevos y sprites de otros
#### personajes se definen en recursos.rpy.
#### El inventario y el telefono Nokia (sistemas/inventario.rpy y sistemas/telefono_nokia.rpy) se usan desde este capitulo.
####   Tecla I o boton "Inventario" = se puede abrir en cualquier momento.
####   $ add_item("telefono") / $ add_item("bateria", 2, notify=True) / has_item("telefono") / remove_item("bateria")
####   $ change_terror(20) sube la asimilacion (y con eso el Nokia se va corrompiendo)

# TODO: el capitulo 2 todavia no sabe que ruta escogio el jugador en el capitulo 1. Solo se puede saber si tomo el celular
# (has_item("telefono")) y cuanta asimilacion trae (asimilacion: ruta A = 10, ruta B = 50, ruta C = 80).
# Si se necesita mas, crear una variable en sistemas_demo.rpy (ej. default cap1_ruta = None) y ponerle valor en cada ruta.

# ============================================================
# CAPÍTULO 2 -
# ============================================================

label capitulo_2:

    # ========================================================
    # ESCENA DE PRUEBA DEL TELEFONO / INVENTARIO
    # Es TEMPORAL: sirve para probar el inventario y el Nokia. Cuando se escriba el capitulo 2 de verdad,
    # borrar desde aqui hasta "FIN DE LA ESCENA DE PRUEBA" (o dejar solo lo que se quiera conservar).
    # ========================================================

    scene bg2
    show mc neutral

    "Sigo dentro del puesto de helados. La puerta está cerrada, pero el silencio de la plaza se siente pegado a mi espalda."

    # Si el jugador no tomó el celular en el capitulo 1 (rutas B y C) lo consigue aqui para poder probarlo.
    if not has_item("telefono"):

        show mc incomodo

        "{color=[thought_color]}\"Ese teléfono no me va a dejar en paz.\"{/color}"
        "{color=[thought_color]}\"Lo dejé... o lo tiré. ¿Entonces por qué sigo escuchándolo?\"{/color}"

        "Me acerco y lo tomo con dos dedos, como si fuera a morderme."

        # TODO: en la ruta B el celular esta en el mostrador y en la ruta C dentro del bote de basura, ajustar el texto segun la ruta.
        $ add_item("telefono", notify=True)

    else:

        show mc neutral

        "{color=[thought_color]}\"Todavía tengo el teléfono en el bolsillo.\"{/color}"

    show mc analizando

    "Lo miro con más calma."

    "{color=[thought_color]}\"Vibraba hace un rato, pero la pantalla está completamente apagada.\"{/color}"
    "{color=[thought_color]}\"Seguro no tiene batería. ¿Cómo pudo vibrar entonces?\"{/color}"
    "{color=[thought_color]}\"Aquí abajo, en el cajón del mostrador, siempre hay pilas de repuesto.\"{/color}"

    "Abro el cajón y saco un par de baterías."

    $ add_item("bateria", 2, notify=True)

    show mc pensante

    "{color=[thought_color]}\"Ojalá le sirvan. Si consigo encenderlo, quizá me diga qué es esa cosa de la asimilación.\"{/color}"

    # TODO: esto es una guia temporal para el jugador, cambiarla por un tutorial mas bonito.
    "{i}(Presiona la tecla I o el botón Inventario para abrir el inventario. Selecciona la batería y pulsa USAR. Después selecciona el teléfono y pulsa ENCENDER. Se apaga con APAGAR o con Escape.){/i}"

    jump cap2_prueba_telefono


# ------------------------------------------------------------
# Menu de prueba: se puede repetir cuantas veces se quiera
# ------------------------------------------------------------

label cap2_prueba_telefono:

    menu:

        "PRUEBA DEL TELÉFONO. Recuerda que el inventario se abre con la tecla I en cualquier momento."

        "Sumar 25%% de asimilación.":

            $ change_terror(25)

            call cap2_expresion_por_asimilacion

            "{color=[thought_color]}\"Siento como si algo me observara desde el teléfono.\"{/color}"

            "(Asimilación: [asimilacion]%%)"

            jump cap2_prueba_telefono

        "Restar 25%% de asimilación.":

            $ change_terror(-25)

            call cap2_expresion_por_asimilacion

            "{color=[thought_color]}\"Respiro hondo. Por un momento, todo se siente un poco más normal.\"{/color}"

            "(Asimilación: [asimilacion]%%)"

            jump cap2_prueba_telefono

        "Conseguir otra batería.":

            $ add_item("bateria", 1, notify=True)

            "{color=[thought_color]}\"Encontré otra pila al fondo del cajón. Con esto debería aguantar un rato más.\"{/color}"

            jump cap2_prueba_telefono

        "Terminar la prueba.":

            "{color=[thought_color]}\"Por ahora es todo lo que puedo hacer con esto.\"{/color}"

            jump cap2_fin_prueba


# La expresion del MC cambia segun la asimilacion (misma escala que el glitch del Nokia)
label cap2_expresion_por_asimilacion:

    if asimilacion >= 100:
        show mc colapso
    elif asimilacion >= 75:
        show mc aterrado
    elif asimilacion >= 50:
        show mc asustado
    elif asimilacion >= 25:
        show mc nervioso
    else:
        show mc pensante

    return


# ============================================================
# FIN DE LA ESCENA DE PRUEBA
# ============================================================

label cap2_fin_prueba:

    # TODO: escribir aqui (o antes) el resto del capitulo 2

    # Mientras no este escrito, el juego regresa al menu principal al llegar aqui.
    return
