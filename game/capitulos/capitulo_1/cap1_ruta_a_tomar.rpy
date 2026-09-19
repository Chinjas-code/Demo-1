##### CAPITULO 1 - RUTA A: TOMAR EL CELULAR #####
#### Se llega desde el menu de cap1_inicio.rpy. Termina en "jump capitulo_2".

# ============================================================
# RUTA A - TOMAR EL CELULAR
# ============================================================

label tomar_celular:

    scene bg2
    show mc neutral

    "Tomo el teléfono."

    # El teléfono pasa al inventario (tecla I). Sin batería no se puede encender, ver sistemas/inventario.rpy
    $ add_item("telefono", notify=True)

    show mc pensante

    "{color=[thought_color]}\"Probablemente tenga algún uso.\"{/color}"
    "{color=[thought_color]}\"Será mejor tener esto que no tener nada.\"{/color}"

    show mc analizando

    "Observé el dispositivo durante unos segundos."

    "{color=[thought_color]}\"Es demasiado raro que todavía no encuentre el mío.\"{/color}"
    "{color=[thought_color]}\"Ni siquiera sé dónde podría estar, tal vez la gerente realmente se lo llevó.\"{/color}"

    # TODO SFX: vibración del celular

    show mc alerta

    "De repente, el teléfono vibró."

    "Me quedo inmóvil."

    "{color=[thought_color]}\"...¿Qué?\"{/color}"

    "Observé la pantalla."

    "No había ninguna notificación visible."

    "Tampoco parecía tener señal."

    # TODO SFX: segunda vibración

    show mc incomodo
    # TODO miedo("incomodo")

    "Entonces volvió a vibrar."

    "{color=[thought_color]}\"Mierda, cualquier cosa ya me asusta.\"{/color}"

    "Me guardo rápidamente el teléfono en el bolsillo."

    "{color=[thought_color]}\"Me voy.\"{/color}"
    "{color=[thought_color]}\"Ya tuve suficiente por este turno.\"{/color}"


    # ========================================================
    # SALIDA DE LA TIENDA
    # ========================================================

    # TODO BG: plaza después del apagón, un pasillo (todavia no hay imagen, sigue el BG del mostrador)

    "Me dirigí rápidamente hacia la salida ubicada al otro extremo de la plaza."

    "Cada paso se sentía más pesado que el anterior."

    "No sabía por qué, el cansancio debe estar afectándome."

    # TODO SFX: vibración del celular

    "El celular volvió a vibrar."

    "{color=[thought_color]}\"¿Qué se supone que le pasa a esto?\"{/color}"

    "Me saqué el teléfono del bolsillo."

    "Una notificación apareció en la pantalla."

    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE / EFECTO: pantalla del celular (usar items/celular.enfrente.png o un screen con el %)
    $ asimilacion = 10

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    show mc nervioso
    # TODO miedo("nervioso")

    mc "¿Qué?"

    "Levanté lentamente la mirada."

    "Frente a mí, a pocos metros de distancia, se encontraba la puerta de salida."

    "Sin embargo, algo se movía alrededor mío."

    "La poca luz que quedaba permitía distinguir algo que no lograba entender."

    #TODO Aqui quisiera intentar un efecto donde se quita el fondo que este ahora mismo puesto como un parpadeo ya que siento que podria ser util,
    # Basicamente seria como una transicion digamos que en bg1 esta todo normal pero se parpadea y ahora sale el infectado con efecto de estatica en ese mismo BG

    # TODO BG: pasillo con infectado con efecto de distorsion y estatica, si se puede
    # ya veremos si sabemos animar los bg
    "Parecía una rueda de automóvil girando lentamente y retorciéndose."

    "Un espiral."

    "Una masa retorcida que se estrangulaba sobre sí misma para avanzar."

    "El movimiento no tenía sentido."

    "Tal vez un vórtice de carne sería la única manera de describirlo."

    show mc asustado
    # TODO miedo("asustado")

    "Permanecí inmóvil ante semejante vista."

    "{color=[thought_color]}\"No.\"{/color}"
    "{color=[thought_color]}\"No, no, no.\"{/color}"

    "La forma continuaba moviéndose hacia mí."

    "Sentí que algo dentro de mí reconocía aquella presencia como alguien que llegué a ver."

    # TODO IMAGE: infectado bloqueando la salida
    # TODO BG: salida de la plaza


    # ========================================================
    # LA PLAZA
    # ========================================================

    "Retrocedí rápidamente."

    "{color=[thought_color]}\"No voy a acercarme a eso.\"{/color}"
    "{color=[thought_color]}\"Ni de puta casualidad.\"{/color}"

    "Decidí regresar hacia el puesto de helados."

    "Sin embargo, algo había cambiado."

    # TODO BG: diferentes pasillos de la plaza

    "Por los diferentes pasillos de la plaza comenzaron a aparecer masas en movimiento."

    "Una."

    "Dos."

    "Tres."

    show mc aterrado

    "Miré hacia los distintos corredores."

    "No podía distinguir exactamente qué eran."

    "Todas se movían de una manera similar."

    "Retorciéndose."

    "Girando."

    "Desplazándose lentamente por todos lados."

    show mc aterrorizado
    # TODO miedo("aterrorizado")

    "Estaba completamente espantado."

    "Sin comprensión de mi alrededor."

    "{color=[thought_color]}\"¿Qué mierda está pasando?\"{/color}"

    # TODO EFFECT: ligera distorsión de pantalla

    scene bg1
    show mc aterrado_2

    "Terminé llegando a mi puesto de helados y rápidamente cerré la puerta."

    # TODO SFX: vibración del celular

    "El teléfono volvió a vibrar."

    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2

