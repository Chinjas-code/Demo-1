# ============================================================
# INVENTARIO
#
# Sistema hecho por un companero (antes "Sistema Inventario"), integrado a la DEMO 1.
# Aqui esta: los objetos, las funciones para agregar / quitar / usar objetos y la pantalla del inventario.
# El telefono Nokia (pantalla, glitch y bateria) esta en telefono_nokia.rpy
#
# COMO SE USA:
#   - En cualquier momento del juego: tecla I  o el boton "Inventario" del menu rapido de abajo.
#   - En el script:
#         $ add_item("telefono")                       # agrega un objeto
#         $ add_item("bateria", 2, notify=True)         # agrega 2 y avisa "Objeto obtenido"
#         $ remove_item("bateria")                     # quita 1
#         if has_item("telefono"):                     # revisa si lo tiene
#   - Para agregar un objeto NUEVO: ponerlo en inventory_items (abajo), poner su imagen en images/items/
#     y agregar su boton en la pantalla "inventory" (copiar el bloque de BATERIA).
# ============================================================


# ============================================================
# VARIABLES
# ============================================================

default inventory = {}
default selected_item = None


# ============================================================
# OBJETOS
# ============================================================

init python:

    inventory_items = {

        "telefono": {
            "name": "TELÉFONO ANTIGUO",
            "description": "Un viejo teléfono móvil. La pantalla está rayada y parece tener muchos años.",
            "image": "images/items/telefono.png"
        },

        "bateria": {
            "name": "BATERÍA",
            "description": "Una batería compatible con el teléfono antiguo.",
            "image": "images/items/bateria.png"
        }

    }


# ============================================================
# FUNCIONES DEL INVENTARIO
# ============================================================

init python:

    def add_item(item_id, amount=1, notify=False):

        if item_id not in inventory_items:
            return

        if item_id not in inventory:
            inventory[item_id] = 0

        inventory[item_id] += amount

        if notify:
            renpy.notify("Objeto obtenido: " + inventory_items[item_id]["name"] + " x" + str(amount))

        renpy.restart_interaction()


    def remove_item(item_id, amount=1):

        global selected_item

        if item_id not in inventory:
            return

        inventory[item_id] -= amount

        if inventory[item_id] <= 0:

            del inventory[item_id]

            if selected_item == item_id:
                selected_item = None

        renpy.restart_interaction()


    def has_item(item_id):

        return inventory.get(item_id, 0) > 0


# ============================================================
# USAR OBJETOS
# ============================================================

init python:

    def use_item(item_id):

        global phone_battery
        global selected_item
        global phone_app


        # ----------------------------------------------------
        # TELÉFONO
        # ----------------------------------------------------

        if item_id == "telefono":

            if not has_item("telefono"):

                renpy.notify("No tienes el teléfono.")
                return


            if phone_battery <= 0:

                renpy.notify("El teléfono no tiene batería.")
                return


            phone_app = "inicio"
            selected_item = None

            renpy.hide_screen("inventory")
            renpy.show_screen("phone_menu")

            renpy.restart_interaction()


        # ----------------------------------------------------
        # BATERÍA
        # ----------------------------------------------------

        elif item_id == "bateria":

            if not has_item("bateria"):

                selected_item = None

                renpy.notify("No tienes baterías.")

                renpy.restart_interaction()

                return


            if not has_item("telefono"):

                renpy.notify("No tienes un teléfono.")
                return


            if phone_battery >= 100:

                renpy.notify("La batería del teléfono está llena.")
                return


            remove_item("bateria", 1)

            phone_battery += 50


            if phone_battery > 100:
                phone_battery = 100


            renpy.notify(
                "Batería instalada. "
                + str(phone_battery)
                + "% de carga."
            )


# ============================================================
# INVENTARIO (PANTALLA)
# ============================================================

screen inventory():

    modal True
    zorder 95


    key "i" action [
        SetVariable("selected_item", None),
        Hide("inventory")
    ]


    add Solid("#000000CC")


    frame:

        xalign 0.5
        yalign 0.5

        xsize 1000
        ysize 600

        background "#101010"

        padding (25, 25)


        vbox:

            spacing 20


            text "INVENTARIO":

                xalign 0.5
                size 40
                color "#DDDDDD"


            frame:

                xfill True
                ysize 2
                background "#444444"


            hbox:

                spacing 25


                # =============================================
                # OBJETOS
                # =============================================

                frame:

                    xsize 600
                    ysize 430

                    background "#080808"

                    padding (15, 15)


                    grid 3 2:

                        spacing 15


                        # =====================================
                        # TELÉFONO
                        # =====================================

                        if has_item("telefono"):

                            button:

                                xsize 175
                                ysize 190

                                action SetVariable(
                                    "selected_item",
                                    "telefono"
                                )


                                if selected_item == "telefono":
                                    background "#383838"
                                else:
                                    background "#181818"


                                hover_background "#444444"


                                vbox:

                                    spacing 8


                                    add inventory_items["telefono"]["image"]:

                                        xsize 100
                                        ysize 100
                                        xalign 0.5


                                    text "TELÉFONO":

                                        xalign 0.5
                                        size 17
                                        color "#CCCCCC"


                                    text "x[inventory.get('telefono', 0)]":

                                        xalign 0.5
                                        size 18
                                        color "#888888"


                        else:

                            frame:

                                xsize 175
                                ysize 190

                                background "#0D0D0D"


                                text "VACÍO":

                                    xalign 0.5
                                    yalign 0.5

                                    size 18
                                    color "#333333"


                        # =====================================
                        # BATERÍA
                        # =====================================

                        if has_item("bateria"):

                            button:

                                xsize 175
                                ysize 190

                                action SetVariable(
                                    "selected_item",
                                    "bateria"
                                )


                                if selected_item == "bateria":
                                    background "#383838"
                                else:
                                    background "#181818"


                                hover_background "#444444"


                                vbox:

                                    spacing 8


                                    add inventory_items["bateria"]["image"]:

                                        xsize 100
                                        ysize 100
                                        xalign 0.5


                                    text "BATERÍA":

                                        xalign 0.5
                                        size 17
                                        color "#CCCCCC"


                                    text "x[inventory.get('bateria', 0)]":

                                        xalign 0.5
                                        size 18
                                        color "#888888"


                        else:

                            frame:

                                xsize 175
                                ysize 190

                                background "#0D0D0D"


                                text "VACÍO":

                                    xalign 0.5
                                    yalign 0.5

                                    size 18
                                    color "#333333"


                        # =====================================
                        # VACÍOS
                        # =====================================

                        frame:
                            xsize 175
                            ysize 190
                            background "#0D0D0D"

                        frame:
                            xsize 175
                            ysize 190
                            background "#0D0D0D"

                        frame:
                            xsize 175
                            ysize 190
                            background "#0D0D0D"

                        frame:
                            xsize 175
                            ysize 190
                            background "#0D0D0D"


                # =============================================
                # INFORMACIÓN
                # =============================================

                frame:

                    xsize 325
                    ysize 430

                    background "#0A0A0A"

                    padding (20, 20)


                    if selected_item == "telefono" and has_item("telefono"):

                        vbox:

                            spacing 15


                            text "TELÉFONO ANTIGUO":

                                size 25
                                color "#DDDDDD"


                            add inventory_items["telefono"]["image"]:

                                xsize 150
                                ysize 150
                                xalign 0.5


                            text "BATERÍA:":

                                size 16
                                color "#888888"


                            text "[phone_battery]%":

                                size 25
                                color "#CCCCCC"


                            text inventory_items["telefono"]["description"]:

                                size 17
                                color "#999999"


                            if phone_battery > 0:

                                textbutton "ENCENDER":

                                    xalign 0.5

                                    action Function(
                                        use_item,
                                        "telefono"
                                    )


                            else:

                                textbutton "SIN BATERÍA":

                                    xalign 0.5

                                    action Function(
                                        use_item,
                                        "telefono"
                                    )


                    elif selected_item == "bateria" and has_item("bateria"):

                        vbox:

                            spacing 15


                            text "BATERÍA":

                                size 25
                                color "#DDDDDD"


                            add inventory_items["bateria"]["image"]:

                                xsize 150
                                ysize 150
                                xalign 0.5


                            text "CANTIDAD: [inventory.get('bateria', 0)]":

                                size 18
                                color "#888888"


                            text inventory_items["bateria"]["description"]:

                                size 17
                                color "#999999"


                            textbutton "USAR":

                                xalign 0.5

                                action Function(
                                    use_item,
                                    "bateria"
                                )


                    else:

                        vbox:

                            xalign 0.5
                            yalign 0.5

                            spacing 15


                            text "NINGÚN OBJETO":

                                xalign 0.5
                                size 22
                                color "#555555"


                            text "Selecciona un objeto":

                                xalign 0.5
                                size 17
                                color "#444444"


            textbutton "CERRAR  [[I]":

                xalign 0.5

                action [
                    SetVariable("selected_item", None),
                    Hide("inventory")
                ]


# ============================================================
# TECLA I
# ============================================================

screen inventory_key():

    key "i" action ToggleScreen("inventory")


# ============================================================
# DISPONIBLE EN CUALQUIER MOMENTO
# Al registrarla como overlay, la tecla I funciona siempre que se este jugando (no en el menu principal),
# sin tener que hacer "show screen inventory_key" en el script.
# ============================================================

init python:

    config.overlay_screens.append("inventory_key")
