##### CAPITULO 1 - INICIO #####
#### Este archivo tiene el inicio del capitulo 1 (la plaza, el celular y la decision de que hacer con el).
#### De aqui el jugador se va a una de las 3 rutas, cada una en su archivo:
####   Tomar el celular     -> label tomar_celular   -> cap1_ruta_a_tomar.rpy
####   Dejarlo donde esta   -> label dejar_celular   -> cap1_ruta_b_dejar.rpy   (y sus subrutas b1, b2, b2_a, b2_b, b2_c)
####   Tirarlo a la basura  -> label tirar_celular   -> cap1_ruta_c_tirar.rpy   (y sus subrutas c1, c2, c2_a, c2_b)
#### Todas las rutas terminan en "jump capitulo_2" o en un final (finales/finales.rpy).
#### Se entra a este archivo desde "label start" que esta en script.rpy.

# ============================================================
# CAPÍTULO 1 - Decisiones del jugador con la asimilación
#============================================================

label capitulo_1:

    scene bg1

    "La noche había caído."

    "Sin explicación alguna, la plaza quedó sumida en un silencio sepulcral."

    "Una oscuridad extraña había invadido gran parte del lugar."
    "Pocas luces continuaban funcionando, parpadeando de manera intermitente."

    # TODO SFX: ambiente de plaza vacia / zumbido de luces
    # TODO BG: este es el interior del puesto de helados, falta el BG de la plaza oscura para esta escena

    show mc neutral

    "Dejé de caminar."

    show mc pensante

    "{color=[thought_color]}\"Yo sé que esta situación no es normal.\"{/color}"
    "{color=[thought_color]}\"Lo sé muy bien.\"{/color}"
    "{color=[thought_color]}\"Y sé que incluso ella tampoco lo es.\"{/color}"
    "{color=[thought_color]}\"No tiene ningún sentido la forma en que interactúa conmigo cuando pide helados.\"{/color}"

    show mc alerta

    "Decidí mirar a mi alrededor."

    "Ni siquiera un apagón debería hacer que un lugar se sintiera así de abrumador, era un ambiente muy pesado."

    show mc incomodo
    # TODO miedo("incomodo")

    "{color=[thought_color]}\"Esto da maldito miedo.\"{/color}"
    "{color=[thought_color]}\"Tengo que salir de aquí. No quiero ver como todo se desaparece de nuevo.\"{/color}"

    "Decidí regresar rápidamente hacia el puesto de helados por mis cosas."

    scene bg2
    show mc alerta

    "Al entrar nuevamente a la tienda, algo llamó mi atención."

    "Sobre el mostrador continuaba el celular antiguo que un cliente había olvidado."

    "El mismo teléfono que nadie parecía reclamar, bastante extraño."

    show mc analizando

    "Permanezco observándolo durante unos segundos."

    "No sabía exactamente para qué, pero podría resultarme útil."

    "{color=[thought_color]}\"¿Por qué sigue aquí?\"{/color}"
    "{color=[thought_color]}\"¿Y por qué nadie ha venido a buscarlo? Aunque tampoco me extraña viendo lo feo que es.\"{/color}"

    "Me acerco lentamente al mostrador."

    # Sin sprite del MC en esta escena para que no tape el celular del BG
    scene bgcelular

    menu:

        "¿QUÉ HACER CON EL CELULAR?"

        "Tomarlo.":
            jump tomar_celular

        "Dejarlo donde está.":
            jump dejar_celular

        "Tirarlo a la basura.":
            jump tirar_celular

