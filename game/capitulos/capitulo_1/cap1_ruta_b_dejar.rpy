##### CAPITULO 1 - RUTA B: DEJAR EL CELULAR #####
#### Se llega desde el menu de cap1_inicio.rpy. Aqui estan todas las subrutas de B:
####   ruta_b1_regresar    -> termina en "jump capitulo_2"
####   ruta_b2_dialogar    -> abre otro menu con ruta_b2_a, ruta_b2_b y ruta_b2_c
####   ruta_b2_a / ruta_b2_b -> terminan en "jump capitulo_2"
####   ruta_b2_c           -> jump final_1_asimilacion (finales/finales.rpy)

# ============================================================
# RUTA B - DEJAR EL CELULAR
# ============================================================

label dejar_celular:

    # BG: mostrador con celular (sigue puesto bgcelular), el MC va a la izquierda para no tapar el celular
    show mc neutral at left

    "Observé el teléfono durante unos segundos más."

    "Después aparté la mirada."

    show mc incomodo
    # TODO miedo("incomodo")

    "{color=[thought_color]}\"Mejor no tocar esa mierda.\"{/color}"

    "Decidí no tocarlo."

    "{color=[thought_color]}\"Seguro alguien va a venir por él.\"{/color}"
    "{color=[thought_color]}\"Y si no, supongo que al rato puedo hacer algo más.\"{/color}"

    "Salgo rápidamente de la tienda."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # TODO BG: plaza después del apagón (todavia no hay imagen)

    "Caminé hacia la salida al otro extremo de la plaza."

    "Cada paso se sentía pesado y cansado."

    # TODO EFFECT: luces parpadeando

    "Las luces comenzaron a parpadear con mayor frecuencia."

    # Ya salí de la tienda, el MC vuelve al centro (antes iba a la izquierda para no tapar el celular del BG)
    show mc pensante at center

    "{color=[thought_color]}\"Aunque no me hubiera venido mal intentar llamar con ese celular.\"{/color}"

    # TODO SFX: apagón
    # TODO EFFECT: parpadeo de pantalla

    "Todas las luces de la plaza se apagaron al mismo tiempo."

    show mc incomodo
    # TODO miedo("incomodo")

    mc "Mierda."

    mc "Lo que faltaba."

    "Durante unos segundos no pude ver absolutamente nada."

    # TODO SFX: sonido de masa retorciéndose

    show mc nervioso
    # TODO miedo("nervioso")

    "Entonces escuché un sonido de algo parecido a nudos retorciéndose."

    "Como si una masa enorme se moviera lentamente en la oscuridad."

    "El sonido provenía de algún lugar cercano."

    # ========================================================
    # EL INFECTADO 1
    # ========================================================

    # TODO SPRITE: INFECTADO 1 (base, sin glitch)
    # TODO BG: plaza completamente oscura con poca luz
    # TODO EFFECT: pantalla oscura leve estatica

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "Me asustó."

    show mc hablando2

    mc "Buenas noches."

    mc "Estaba buscando la salida."

    mc "Me quedé hasta tarde."

    show mc incomodo
    # TODO miedo("incomodo")

    "Era incómodo."

    "Extremadamente incómodo."

    "Hablar con alguien en medio de una plaza completamente a oscuras. ¿Qué sentido tiene?"

    "Pero había algo más."

    infectado1 "Buenas noches."

    infectado1 "¿Usted de dónde trabaja?"

    infectado1 "Esta tienda debió cerrar hace tiempo."

    infectado1 "Desde que se quedó hasta tarde."

    "El silencio que siguió fue aún más incómodo."

    "Intenté mantener la calma."

    show mc hablando2

    mc "Trabajo en el puesto de helados de aquí atrás."

    mc "¿Tendrá una lámpara?"

    "La voz permaneció en silencio durante unos segundos."

    # TODO EFFECT: distorsión
    # TODO SPRITE: infectado 1 modificado con cabeza alargada

    infectado1 "Buenas noches..."

    infectado1 "Buenas noches..."

    infectado1 "En este lugar es tarde para que se encuentre..."

    infectado1 "¿Por qué no encuentra uno de chocolate?"

    show mc asustado
    # TODO miedo("asustado")

    "Me quedé inmóvil."

    "Las palabras no tenían sentido."

    "Pero una parte de mí comenzaba a comprender algo."

    "Esto no estaba bien."

    "Nada estaba bien."

    "Ni siquiera desde el principio."

    "{color=[thought_color]}\"Mierda.\"{/color}"
    "{color=[thought_color]}\"¿Por qué no me di cuenta antes?\"{/color}"


    # ========================================================
    # DECISIÓN DEL JUGADOR
    # ========================================================

    menu:

        "¿QUÉ HACER?"

        "Regresar caminando hacia la tienda.":
            jump ruta_b1_regresar

        "Continuar dialogando con la voz.":
            jump ruta_b2_dialogar


# ============================================================
# RUTA B1 - REGRESAR A LA TIENDA
# ============================================================

label ruta_b1_regresar:

    show mc aterrado

    "Sin pensarlo dos veces, comencé a caminar en dirección al puesto de helados."

    "No quería seguir ahí."

    "La memoria muscular funcionó antes que el pensamiento."

    "Mis piernas comenzaron a moverse rápidamente."

    # TODO SFX: masa retorciéndose
    # TODO BG: MC huyendo de infectado 1 en medio de la plaza medio apagada, la cabeza debe estar por arriba con el cuello por todos lados

    "Mientras avanzaba, el sonido de la masa retorciéndose aumentó."

    "Un poco más fuerte y más fuerte."

    "Me está siguiendo."

    infectado1 "Buenos días."

    infectado1 "¿Uno de chocolate con su gente?"

    infectado1 "¿Por qué es tarde?"

    show mc aterrado_2
    # TODO miedo("aterrorizado")  (aterrado todavia no esta en la tabla)

    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"Solo sigue corriendo.\"{/color}"

    "Finalmente llegué a la tienda."

    # TODO SFX: puerta cerrándose

    scene bg1
    show mc aterrado

    "Entré y cerré la puerta de golpe."

    "Permanecí apoyado contra ella recuperando el aliento, completamente agitado."

    # TODO SFX: vibración

    show mc nervioso_2

    mc "¿Una vibración?"

    "Provenía del interior del local."

    "El sonido venía del interior de la tienda."

    "Volteé lentamente."

    "El celular estaba vibrando constantemente."

    show mc asustado
    # TODO miedo("asustado")

    "{color=[thought_color]}\"¿Asimilación?\"{/color}"


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE: celular con % de asimilacion
    $ asimilacion = 50

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    # TODO SFX: vibración continua

    "La vibración continuó."

    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2


# ============================================================
# RUTA B2 - CONTINUAR DIALOGANDO CON LA VOZ
# ============================================================

label ruta_b2_dialogar:

    # TODO SFX: masa retorciendose

    show mc nervioso

    "Decidí no moverme."

    "No tenía otra idea de qué otra cosa hacer."

    show mc hablando1

    mc "¿Disculpe?"

    "La voz permaneció en silencio."

    "El sonido de algo retorciéndose continuaba alrededor."

    # TODO SPRITE: infectado1 neutral

    infectado1 "Buenas noches."

    mc "¿Usted sabe dónde está la salida?"

    "Silencio."

    mc "¿Se encuentra bien?"

    "La voz comenzó a responder lentamente."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    show mc incomodo

    "{color=[thought_color]}\"Está repitiendo lo mismo.\"{/color}"
    "{color=[thought_color]}\"¿Está menso?\"{/color}"

    infectado1 "¿Usted trabaja aquí?"

    show mc hablando2

    mc "Sí."

    mc "En la tienda de helados."

    infectado1 "¿Uno de chocolate?"

    show mc nervioso_2
    # TODO miedo("nervioso")

    "Tragué saliva, algo no me gustaba."

    mc "No."

    mc "Bueno..."

    mc "Hoy ya cerramos."

    "La voz permaneció en silencio."

    # TODO SFX: golpe suave contra una pared

    show mc asustado
    # TODO miedo("asustado")

    "Entonces algo golpeó por todos lados."

    mc "¿Hola?"

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    "Las palabras comenzaron a repetirse."

    "Cada vez más rápido."

    "Cada vez menos humanas."

    # TODO EFFECT: distorsión

    show mc aterrado_2

    "{color=[thought_color]}\"No quiero estar más aquí.\"{/color}"
    "{color=[thought_color]}\"Pero si le doy la espalda...\"{/color}"


    # ========================================================
    # DECISIÓN POR TIEMPO
    # ========================================================

    # TODO: convertir este menú en una decisión con temporizador

    menu:

        "¿QUÉ HACER?"

        "Regresar caminando hacia la tienda.":
            jump ruta_b2_a

        "Continuar dialogando con la voz.":
            jump ruta_b2_b

        "No hacer nada.":
            jump ruta_b2_c


# ============================================================
# RUTA B2-A - REGRESAR A LA TIENDA
# ============================================================

label ruta_b2_a:

    show mc aterrado

    "Decidí regresar sin pensarlo mucho y caminar."

    "La voz continuaba detrás de mí."

    infectado1 "Buenas noches."

    infectado1 "¿Uno de chocolate?"

    infectado1 "Buenas noches."

    # TODO SFX: masa retorciéndose aumentando
    # TODO BG: MC huyendo de infectado 1 en medio de la plaza medio apagada, la cabeza debe estar por arriba con el cuello por todos lados

    show mc aterrorizado
    # TODO miedo("aterrorizado")

    "¿Caminar? Decidí correr por mi vida."

    "Sentía que alrededor mío había algo moviéndose."

    scene bg1
    show mc aterrado_2

    "Al llegar a la tienda, cerré la puerta de golpe."

    "Permanecí completamente perturbado y agitado."

    # TODO SFX: vibración

    "Entonces escuché una vibración."

    "El celular que estaba en la tienda parece que recibió algo."

    "Aun con miedo, decidí acercarme lentamente al teléfono."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE: celular con notificación
    # TODO: el MC viendo el celular (BG o sprite de cerca)

    show mc analizando

    "Observé el teléfono."

    "La pantalla mostraba una notificación nueva."

    $ asimilacion = 50

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    show mc asustado
    # TODO miedo("asustado")

    "{color=[thought_color]}\"¿Qué significa esto?\"{/color}"
    "{color=[thought_color]}\"No, más bien ¿Qué mierda era esa persona?\"{/color}"

    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2


# ============================================================
# RUTA B2-B - CONTINUAR DIALOGANDO
# ============================================================

label ruta_b2_b:

    show mc nervioso

    "Permanezco frente a la oscuridad con poca luz alrededor mío."

    "Intento mantener la tranquilidad."

    show mc hablando2

    mc "¿Usted trabaja aquí?"

    "..."

    infectado1 "Buenas noches."

    mc "¿Qué está haciendo en esta plaza, trabaja aquí?"

    "..."

    show mc hablando1

    mc "¿Hola?"

    # TODO BG: infectado 1 rodeando al MC con el cuello por todos lados

    show mc asustado
    # TODO miedo("asustado")

    "El sonido alrededor comenzó a hacerse más fuerte, de nudos y carne."

    "Como si algo enorme se estuviera moviendo por las paredes."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "{color=[thought_color]}\"Esto no tiene sentido.\"{/color}"
    "{color=[thought_color]}\"No fue buena idea hablar.\"{/color}"

    "Miré hacia la oscuridad."

    show mc hablando2

    mc "¿Quiere uno de chocolate?"

    "Silencio absoluto."


    infectado1 "Buenas noches."

    infectado1 "Uno de chocolate."

    # TODO EFFECT: distorsión de voz

    infectado1 "Uno de chocolate."

    infectado1 "Uno de chocolate."

    infectado1 "UNO DE CHOCOLATE."

    infectado1 "UN0 D3 C'¿+´lA7E@"

    show mc aterrado
    # TODO miedo("aterrorizado")  (aterrado todavia no esta en la tabla)

    "{color=[thought_color]}\"No debí decir eso.\"{/color}"

    "Decidí correr hacia la salida de la plaza sin importar nada."

    "Aunque claramente no veía la salida, recordaba aproximadamente dónde ir, aunque también..."

    "Hay algo moviéndose por todos lados."

    "{color=[thought_color]}\"Mierda, mierda.\"{/color}"

    scene bg1
    show mc aterrado_2

    "Al llegar a la salida, cierro la puerta de golpe y sigo corriendo con todas mis fuerzas."

    "Pero una agradable vista de helados con un toque de vainilla inunda mi nariz."

    show mc aterrorizado
    # TODO miedo("aterrorizado")

    "Aunque en vez de tranquilizarme, me da un miedo extremo."

    mc "¿Qué hago aquí?"

    # TODO SFX: vibración

    "Escucho una vibración."

    "El celular que estaba en la tienda parece que recibió algo."

    "Aun con miedo, decido acercarme lentamente al teléfono."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE: celular con notificación
    # TODO: el MC viendo el celular (BG o sprite de cerca)

    show mc analizando

    "La pantalla mostraba una notificación nueva."

    $ asimilacion = 50

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    show mc asustado
    # TODO miedo("asustado")

    "{color=[thought_color]}\"¿Qué significa esto?\"{/color}"
    "{color=[thought_color]}\"No, más bien ¿Qué mierda era esa persona?\"{/color}"


    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2


# ============================================================
# RUTA B2-C - NO HACER NADA
# ============================================================

label ruta_b2_c:

    # TODO BG: infectado 1 rodeando al MC con el cuello por todos lados

    show mc nervioso_2

    "Decidí no responder."

    "No hacer ningún movimiento y quedarme como estatua."

    "..."

    show mc asustado
    # TODO miedo("asustado")

    "Noto lento mi capacidad de pensamiento."

    "Me sentía mareado."

    "Confundido."

    show mc aterrado_2

    "Como si mi cuerpo ya no respondiera correctamente."

    "..."

    "La criatura continuaba observándome."

    infectado1 "¿Se encuentra bien?"

    "Decidí no responder."

    infectado1 "¿Necesita ayuda?"

    "..."

    # TODO: screamer de infectado 1 (imagen + sonido fuerte)

    # TODO EFFECT: distorsión progresiva
    # TODO EFFECT: errores visuales
    # TODO IMAGE: mensaje del ente el mero mero

    show mc colapso_2
    # TODO miedo("colapso")

    "\"¿Quién eres tú?\""

    "..."

    "\"Creo que puedo verte.\""

    "..."

    "\"Tal vez algún día logre entrar ahí también.\""

    # TODO IMAGE: Infectado ocupando pantalla

    #TODO aqui tengo que ver como chingados hago el final 1 que sea un gameover dependiendo las acciones, no se como configurarlo aun pero ya que termine de poner esto bonito lo hare
    # TODO: en vez de mandar siempre al final 1, aqui deberia usar infectado_decide_atacar() (sistemas_demo.rpy) para decidir el final

    jump final_1_asimilacion

