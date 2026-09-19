# ============================================================
# TELEFONO NOKIA
#
# Sistema hecho por un companero (antes "Sistema Inventario"), integrado a la DEMO 1.
# Aqui esta: la bateria del telefono, la pantalla del Nokia (menu, estado, mensajes, notas)
# y los efectos de glitch (con ATL) que cambian segun la ASIMILACION del MC.
#
# La asimilacion es la misma variable "asimilacion" de sistemas_demo.rpy (0 a 100):
#     0-24  normal  |  25-49 glitch leve  |  50-74 glitch medio  |  75-99 glitch fuerte  |  100 maximo
#
# Como se abre: desde el inventario (tecla I) -> seleccionar el telefono -> ENCENDER.
# Necesita bateria: en el inventario seleccionar una BATERIA -> USAR (cada una da 50%).
# Se cierra con APAGAR o con la tecla Escape.
# ============================================================


# ============================================================
# VARIABLES
# ============================================================

default phone_battery = 0

default phone_app = "inicio"
default phone_glitch_phase = 0


# ============================================================
# ============================================================
#
#                   TRANSFORMS GLITCH
#
# ============================================================
# ============================================================


# ------------------------------------------------------------
# GLITCH LEVE
# Pequeño movimiento horizontal.
# ------------------------------------------------------------

transform phone_glitch_light:

    xoffset 0
    yoffset 0
    alpha 1.0

    pause 0.60

    xoffset 2
    pause 0.03

    xoffset -2
    pause 0.03

    xoffset 0
    pause 0.50

    alpha 0.92
    pause 0.04

    alpha 1.0
    pause 0.30

    repeat


# ------------------------------------------------------------
# GLITCH MEDIO
# ------------------------------------------------------------

transform phone_glitch_medium:

    xoffset 0
    yoffset 0
    alpha 1.0

    pause 0.25

    xoffset -4
    pause 0.04

    xoffset 5
    yoffset 1
    pause 0.03

    xoffset 0
    yoffset 0
    pause 0.18

    xoffset 3
    pause 0.03

    xoffset -3
    pause 0.03

    xoffset 0
    pause 0.25

    alpha 0.80
    pause 0.03

    alpha 1.0
    pause 0.15

    repeat


# ------------------------------------------------------------
# GLITCH FUERTE
# ------------------------------------------------------------

transform phone_glitch_strong:

    xoffset 0
    yoffset 0
    alpha 1.0

    pause 0.12

    xoffset -8
    pause 0.025

    xoffset 7
    yoffset -2
    pause 0.025

    xoffset -5
    yoffset 3
    pause 0.025

    xoffset 0
    yoffset 0
    pause 0.10

    alpha 0.60
    pause 0.025

    alpha 1.0

    xoffset 9
    pause 0.025

    xoffset -7
    pause 0.025

    xoffset 0
    pause 0.12

    repeat


# ------------------------------------------------------------
# GLITCH MÁXIMO
# ------------------------------------------------------------

transform phone_glitch_max:

    xoffset 0
    yoffset 0
    alpha 1.0

    pause 0.06

    xoffset -12
    yoffset 2
    pause 0.02

    xoffset 10
    yoffset -3
    pause 0.02

    xoffset -7
    yoffset 4
    pause 0.02

    alpha 0.45
    pause 0.02

    alpha 1.0

    xoffset 13
    yoffset 0
    pause 0.02

    xoffset -10
    yoffset -2
    pause 0.02

    xoffset 4
    yoffset 3
    pause 0.02

    xoffset 0
    yoffset 0

    pause 0.06

    repeat


# ------------------------------------------------------------
# BARRA DE INTERFERENCIA 1
# ------------------------------------------------------------

transform interference_bar_one:

    xpos 10
    ypos 40
    alpha 0.0

    pause 0.20

    alpha 0.85
    ypos 40

    linear 0.10 ypos 330

    alpha 0.0

    pause 0.15

    repeat


# ------------------------------------------------------------
# BARRA DE INTERFERENCIA 2
# ------------------------------------------------------------

transform interference_bar_two:

    xpos 80
    ypos 350
    alpha 0.0

    pause 0.35

    alpha 0.7

    linear 0.08 ypos 100

    alpha 0.0

    pause 0.20

    repeat


# ------------------------------------------------------------
# PARPADEO DE TEXTO CORRUPTO
# ------------------------------------------------------------

transform corrupt_text_flash:

    alpha 0.0
    xoffset 0

    pause 0.35

    alpha 0.0

    pause 0.20

    alpha 1.0
    xoffset -4

    pause 0.05

    alpha 0.0

    pause 0.15

    alpha 1.0
    xoffset 5

    pause 0.04

    alpha 0.0

    pause 0.40

    repeat


# ------------------------------------------------------------
# PARPADEO MUY AGRESIVO
# ------------------------------------------------------------

transform corrupt_text_max:

    alpha 0.0
    xoffset 0
    yoffset 0

    pause 0.10

    alpha 1.0
    xoffset -8

    pause 0.04

    alpha 0.0

    pause 0.05

    alpha 1.0
    xoffset 7
    yoffset -3

    pause 0.04

    alpha 0.0

    pause 0.08

    alpha 1.0
    xoffset -3
    yoffset 2

    pause 0.03

    alpha 0.0

    repeat




# ============================================================
# ============================================================
#
#                    NOKIA
#
# ============================================================
# ============================================================

screen phone_menu():

    modal True
    zorder 100


    key "K_ESCAPE" action [
        SetVariable("phone_app", "inicio"),
        Hide("phone_menu")
    ]


    add Solid("#000000DD")


    # ========================================================
    # CUERPO DEL TELÉFONO
    # ========================================================

    frame:

        xalign 0.5
        yalign 0.5

        xsize 450
        ysize 750

        background "#20262A"

        padding (25, 20)


        vbox:

            xalign 0.5
            spacing 10


            # =================================================
            # NOKIA
            # =================================================

            if asimilacion < 25:

                text "NOKIA":

                    xalign 0.5
                    size 28
                    color "#D0D0D0"


            elif asimilacion < 50:

                text "N0KIA":

                    xalign 0.5
                    size 28
                    color "#D0D0D0"

                    at phone_glitch_light


            elif asimilacion < 75:

                text "N//K!A":

                    xalign 0.5
                    size 28
                    color "#D0D0D0"

                    at phone_glitch_medium


            elif asimilacion < 100:

                text "N#K?A":

                    xalign 0.5
                    size 28
                    color "#D0D0D0"

                    at phone_glitch_strong


            else:

                text "??//??":

                    xalign 0.5
                    size 30
                    color "#D0D0D0"

                    at phone_glitch_max


            # =================================================
            # LCD
            # =================================================

            frame:

                xalign 0.5

                xsize 380
                ysize 440

                background "#9EAD78"

                padding (15, 12)


                # ---------------------------------------------
                # HACER TEMBLAR TODO EL LCD
                # ---------------------------------------------

                if asimilacion < 25:

                    at transform:
                        xoffset 0
                        yoffset 0


                elif asimilacion < 50:

                    at phone_glitch_light


                elif asimilacion < 75:

                    at phone_glitch_medium


                elif asimilacion < 100:

                    at phone_glitch_strong


                else:

                    at phone_glitch_max


                fixed:


                    # =========================================
                    # CONTENIDO NORMAL
                    # =========================================

                    vbox:

                        xfill True
                        spacing 10


                        # =====================================
                        # BARRA SUPERIOR
                        # =====================================

                        hbox:

                            xfill True


                            if asimilacion < 25:

                                text "NO SIGNAL":
                                    size 14
                                    color "#182018"


                            elif asimilacion < 50:

                                text "NO S!GNAL":
                                    size 14
                                    color "#182018"


                            elif asimilacion < 75:

                                text "N# S!GN?L":
                                    size 14
                                    color "#182018"


                            elif asimilacion < 100:

                                text "I SEE YOU":
                                    size 14
                                    color "#182018"


                            else:

                                text "BEHIND YOU":
                                    size 14
                                    color "#182018"


                            null width 80


                            text "BAT [phone_battery]%":
                                size 14
                                color "#182018"


                        frame:

                            xfill True
                            ysize 3

                            background "#182018"


                        # =====================================
                        # MENÚ PRINCIPAL
                        # =====================================

                        if phone_app == "inicio":

                            vbox:

                                xalign 0.5
                                spacing 14


                                null height 10


                                if asimilacion < 25:

                                    text "MENU":
                                        xalign 0.5
                                        size 30
                                        color "#182018"


                                    text "1  ESTADO":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "2  MENSAJES":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "3  NOTAS":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                elif asimilacion < 50:

                                    text "M?NU":
                                        xalign 0.5
                                        size 30
                                        color "#182018"


                                    text "1  ESTAD?":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "2  MENSAJ#S":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "3  N?TAS":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                elif asimilacion < 75:

                                    text "M//NU":
                                        xalign 0.5
                                        size 30
                                        color "#182018"


                                    text "1  E#T?DO":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "2  M#N//JES":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "3  N?T#S":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                elif asimilacion < 100:

                                    text "??//MENU//??":
                                        xalign 0.5
                                        size 25
                                        color "#182018"


                                    text "1  T# EST?DO":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "2  TE VEMOS":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "3  NO MIRES":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                else:

                                    text "ERROR":
                                        xalign 0.5
                                        size 31
                                        color "#182018"


                                    text "1  ########":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "2  BEHIND YOU":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "3  ??//??//??":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                        # =====================================
                        # ESTADO
                        # =====================================

                        elif phone_app == "estado":

                            vbox:

                                xalign 0.5
                                spacing 9


                                if asimilacion < 50:

                                    text "ESTADO":
                                        xalign 0.5
                                        size 27
                                        color "#182018"

                                elif asimilacion < 75:

                                    text "EST?DO":
                                        xalign 0.5
                                        size 27
                                        color "#182018"

                                elif asimilacion < 100:

                                    text "T# EST?DO":
                                        xalign 0.5
                                        size 27
                                        color "#182018"

                                else:

                                    text "ASIMILADO":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                frame:

                                    xfill True
                                    ysize 2
                                    background "#182018"


                                if asimilacion < 75:

                                    text "ASIMILACION DEL TERROR":

                                        xalign 0.5
                                        size 17
                                        color "#182018"

                                else:

                                    text "ASIMIL?CION // T#RROR":

                                        xalign 0.5
                                        size 17
                                        color "#182018"


                                text "[asimilacion]%":

                                    xalign 0.5
                                    size 45
                                    color "#182018"


                                frame:

                                    xalign 0.5

                                    xsize 300
                                    ysize 27

                                    background "#65724F"

                                    padding (3, 3)


                                    bar:

                                        value asimilacion
                                        range 100

                                        xsize 294
                                        ysize 21


                                if asimilacion < 25:

                                    text "ESTABLE":
                                        xalign 0.5
                                        size 24
                                        color "#182018"


                                elif asimilacion < 50:

                                    text "INQUIETO":
                                        xalign 0.5
                                        size 24
                                        color "#182018"


                                elif asimilacion < 75:

                                    text "ALTERADO":
                                        xalign 0.5
                                        size 24
                                        color "#182018"


                                elif asimilacion < 100:

                                    text "CRITICO":
                                        xalign 0.5
                                        size 24
                                        color "#182018"


                                    text "NO CONFIES EN EL TELEFONO":
                                        xalign 0.5
                                        size 14
                                        color "#182018"


                                else:

                                    text "ASIMILADO":
                                        xalign 0.5
                                        size 24
                                        color "#182018"


                                    text "NO MIRES ATRAS":
                                        xalign 0.5
                                        size 17
                                        color "#182018"


                        # =====================================
                        # MENSAJES
                        # =====================================

                        elif phone_app == "mensajes":

                            vbox:

                                xalign 0.5
                                spacing 8


                                if asimilacion < 25:

                                    text "MENSAJES":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    null height 35


                                    text "BANDEJA VACIA":
                                        xalign 0.5
                                        size 19
                                        color "#182018"


                                elif asimilacion < 50:

                                    text "MENS?JES":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "1 MENSAJE":
                                        xalign 0.5
                                        size 18
                                        color "#182018"


                                    text "DESCONOCIDO":
                                        size 14
                                        color "#293529"


                                    text "\"Pu?des v#rme?\"":
                                        size 18
                                        color "#182018"


                                    text "\"No mires atras.\"":
                                        size 16
                                        color "#182018"


                                elif asimilacion < 75:

                                    text "M#NS//J?S":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "3 M#NS?JES":
                                        xalign 0.5
                                        size 18
                                        color "#182018"


                                    text "D?SC#NOCIDO":
                                        size 14
                                        color "#293529"


                                    text "\"N# d?berias est// aqui.\"":
                                        size 16
                                        color "#182018"


                                    text "\"N? m!res el escaparate.\"":
                                        size 16
                                        color "#182018"


                                    text "\"T# v#mos.\"":
                                        size 17
                                        color "#182018"


                                elif asimilacion < 100:

                                    text "M#NS//J?S":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "?? MEN###":
                                        xalign 0.5
                                        size 18
                                        color "#182018"


                                    text "D?SC#NOC!DO":
                                        size 14
                                        color "#293529"


                                    text "\"T# ESTAM#S V!ENDO\"":
                                        size 17
                                        color "#182018"


                                    text "\"D#TR#S D# T!\"":
                                        size 19
                                        color "#182018"


                                    text "\"NO // NO // NO\"":
                                        size 17
                                        color "#182018"


                                    text "\"###########\"":
                                        size 17
                                        color "#182018"


                                else:

                                    text "########":
                                        xalign 0.5
                                        size 28
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "ERROR // ERROR":
                                        xalign 0.5
                                        size 19
                                        color "#182018"


                                    text "D#: ??":
                                        size 16
                                        color "#293529"


                                    text "\"Y# EST#Y AQ##\"":
                                        size 21
                                        color "#182018"


                                    text "\"??//??//??\"":
                                        size 20
                                        color "#182018"


                                    text "\"NO MIRES ATRAS\"":
                                        size 19
                                        color "#182018"


                                    text "\"###########\"":
                                        size 18
                                        color "#182018"


                        # =====================================
                        # NOTAS
                        # =====================================

                        elif phone_app == "notas":

                            vbox:

                                xalign 0.5
                                spacing 8


                                if asimilacion < 25:

                                    text "NOTAS":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    null height 30


                                    text "No hay notas.":
                                        xalign 0.5
                                        size 18
                                        color "#182018"


                                elif asimilacion < 50:

                                    text "N?TAS":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "NOTA 01":
                                        size 17
                                        color "#182018"


                                    text "Enc?ntrar una salida.":
                                        size 16
                                        color "#182018"


                                    text "NOTA 02":
                                        size 17
                                        color "#182018"


                                    text "No mirar atras.":
                                        size 16
                                        color "#182018"


                                elif asimilacion < 75:

                                    text "N#T//S":
                                        xalign 0.5
                                        size 27
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "N#TA 01":
                                        size 17
                                        color "#182018"


                                    text "N# C#NFI#S EN EL T#LEFONO":
                                        size 15
                                        color "#182018"


                                    text "N?TA 02":
                                        size 17
                                        color "#182018"


                                    text "NO M?RES LOS ESP#JOS":
                                        size 15
                                        color "#182018"


                                    text "N?TA 03":
                                        size 17
                                        color "#182018"


                                    text "ALGO TE SIGUE":
                                        size 15
                                        color "#182018"


                                elif asimilacion < 100:

                                    text "??//N#TAS//??":
                                        xalign 0.5
                                        size 25
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "N#TA ??":
                                        size 17
                                        color "#182018"


                                    text "T# YA ESTUV!STE AQUI":
                                        size 17
                                        color "#182018"


                                    text "N#TA ##":
                                        size 17
                                        color "#182018"


                                    text "D#TR#S D# T!":
                                        size 19
                                        color "#182018"


                                    text "N#TA //":
                                        size 17
                                        color "#182018"


                                    text "NO HAY SALIDA":
                                        size 19
                                        color "#182018"


                                else:

                                    text "?????":
                                        xalign 0.5
                                        size 28
                                        color "#182018"


                                    frame:
                                        xfill True
                                        ysize 2
                                        background "#182018"


                                    text "###########":
                                        xalign 0.5
                                        size 18
                                        color "#182018"


                                    text "NO HAY SALIDA":
                                        xalign 0.5
                                        size 21
                                        color "#182018"


                                    text "NO LA NECESITAS":
                                        xalign 0.5
                                        size 19
                                        color "#182018"


                                    text "ESTAS EN CASA":
                                        xalign 0.5
                                        size 23
                                        color "#182018"


                    # =================================================
                    # =================================================
                    #
                    #      CAPAS DE INTERFERENCIA SUPERPUESTAS
                    #
                    # =================================================
                    # =================================================


                    # =========================================
                    # 25% - PRIMERAS INTERFERENCIAS
                    # =========================================

                    if asimilacion >= 25:

                        frame:

                            xsize 110
                            ysize 2

                            background "#182018"

                            at interference_bar_one


                    # =========================================
                    # 50% - SEGUNDA INTERFERENCIA
                    # =========================================

                    if asimilacion >= 50:

                        frame:

                            xsize 230
                            ysize 4

                            background "#182018"

                            at interference_bar_two


                    # =========================================
                    # 50% - TEXTO FANTASMA
                    # =========================================

                    if asimilacion >= 50:

                        text "??//SIGNAL LOST//??":

                            xpos 40
                            ypos 120

                            size 17
                            color "#182018"

                            at corrupt_text_flash


                    # =========================================
                    # 75% - MENSAJE SUPERPUESTO
                    # =========================================

                    if asimilacion >= 75:

                        text "D#TR#S D# T!":

                            xpos 80
                            ypos 220

                            size 25
                            color "#182018"

                            at corrupt_text_flash


                        text "###########":

                            xpos 30
                            ypos 315

                            size 24
                            color "#182018"

                            at corrupt_text_flash


                    # =========================================
                    # 100% - CORRUPCIÓN MÁXIMA
                    # =========================================

                    if asimilacion >= 100:

                        text "??//ERROR//??":

                            xpos 65
                            ypos 70

                            size 28
                            color "#182018"

                            at corrupt_text_max


                        text "TE VEMOS":

                            xpos 105
                            ypos 170

                            size 29
                            color "#182018"

                            at corrupt_text_max


                        text "NO MIRES":

                            xpos 95
                            ypos 270

                            size 31
                            color "#182018"

                            at corrupt_text_max


                        frame:

                            xpos 0
                            ypos 200

                            xsize 350
                            ysize 13

                            background "#182018"

                            at corrupt_text_max


            # =================================================
            # BOTONES
            # =================================================

            hbox:

                xalign 0.5
                spacing 10


                textbutton "1\nESTADO":

                    xsize 105
                    ysize 60

                    text_size 14
                    text_xalign 0.5

                    action SetVariable(
                        "phone_app",
                        "estado"
                    )


                textbutton "2\nMENSAJES":

                    xsize 105
                    ysize 60

                    text_size 12
                    text_xalign 0.5

                    action SetVariable(
                        "phone_app",
                        "mensajes"
                    )


                textbutton "3\nNOTAS":

                    xsize 105
                    ysize 60

                    text_size 14
                    text_xalign 0.5

                    action SetVariable(
                        "phone_app",
                        "notas"
                    )


            hbox:

                xalign 0.5
                spacing 10


                textbutton "4":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action NullAction()


                textbutton "MENU":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action SetVariable(
                        "phone_app",
                        "inicio"
                    )


                textbutton "6":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action NullAction()


            hbox:

                xalign 0.5
                spacing 10


                textbutton "7":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action NullAction()


                textbutton "0":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action NullAction()


                textbutton "9":

                    xsize 105
                    ysize 45

                    text_xalign 0.5

                    action NullAction()


            # =================================================
            # APAGAR
            # =================================================

            textbutton "APAGAR":

                xalign 0.5

                action [
                    SetVariable("phone_app", "inicio"),
                    Hide("phone_menu")
                ]