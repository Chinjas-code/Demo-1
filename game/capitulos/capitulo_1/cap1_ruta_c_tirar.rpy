##### CAPITULO 1 - RUTA C: TIRAR EL CELULAR #####
#### Se llega desde el menu de cap1_inicio.rpy. Aqui estan todas las subrutas de C:
####   ruta_c1_correr      -> termina en "jump capitulo_2"
####   ruta_c2_dialogar    -> abre otro menu con ruta_c2_a y ruta_c2_b
####   ruta_c2_a           -> termina en "jump capitulo_2"
####   ruta_c2_b           -> jump final_1_asimilacion (finales/finales.rpy)
#### (ruta_c2_b tambien se puede llegar directo desde el primer menu de tirar_celular con "No hacer nada")

# ============================================================
# RUTA C - TIRAR EL CELULAR
# ============================================================

label tirar_celular:

    scene bg2
    show mc neutral

    "Tomo el teléfono y sin pensarlo demasiado, lo arrojo dentro del bote de basura."

    show mc incomodo

    "{color=[thought_color]}\"No es lo mismo dejarlo donde estaba que tirarlo a la basura.\"{/color}"
    "{color=[thought_color]}\"...¿Verdad?\"{/color}"

    "Me olvido de eso."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # TODO BG: plaza después del apagón (todavia no hay imagen)

    "Salgo rápidamente de la tienda."

    "Aunque cada paso se sentía más pesado que el anterior."

    show mc nervioso
    # TODO miedo("nervioso")

    "Me empiezo a fatigar y a sentirme mareado."

    "{color=[thought_color]}\"¿Qué está pasando?\"{/color}"

    show mc asustado
    # TODO miedo("asustado")

    "El peso aumentó tan repentinamente que pierdo el equilibrio."

    "Caigo de rodillas sobre el suelo."

    "Durante unos segundos no pude ni moverme."

    mc "¿Qué...?"

    "Intento levantarme pero no puedo."

    # TODO SFX: masa triturándose

    "Entonces escuché un sonido de algo moviéndose por todos lados."

    # ========================================================
    # EL INFECTADO 1 APARECE
    # ========================================================

    # TODO SPRITE: INFECTADO 1
    # TODO BG: plaza / criatura frente al MC viendo directo a la cara y en el piso
    # TODO EFFECT: cuello extendiéndose

    show mc aterrorizado
    # TODO miedo("aterrorizado")

    "Una enorme cara se encontraba suspendida sobre mí."

    "No tenía ojos normales."

    "Y parece que algo que solo con error puede describir la cara de la criatura."

    "Su cuello se extendía por todo el pasillo."

    "Giraba sobre sí mismo."

    "Se expandía, se contraía y se hacía una rueda misma con nudos por todos lados."

    "Desaparecía dentro de las paredes y aparecía por el techo."

    "Era imposible comprender pero un miedo tan extremo empezaba a romperme."

    "El horror recorrió mi cuerpo."

    infectado1 "Buenas tardes."

    infectado1 "¿Estará la gerente?"

    infectado1 "Quiero hablar sobre los horarios de apertura para la siguiente semana."

    show mc aterrado

    "No podía procesar lo que me estaba diciendo."

    "¿Una cosa con cuello infinito me estaba hablando sobre horarios laborales?"

    "{color=[thought_color]}\"¿Qué mierda?\"{/color}"
    "{color=[thought_color]}\"¿Qué estoy viendo?\"{/color}"
    "{color=[thought_color]}\"¿Por qué está hablando como si fuera normal?\"{/color}"

    "La criatura inclinó ligeramente la cabeza."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"


    # ========================================================
    # DECISIÓN POR TIEMPO
    # ========================================================

    # TODO: convertir este menú en una decisión con temporizador

    menu:

        "¿QUÉ HACER?"

        "Intentar correr.":
            jump ruta_c1_correr

        "Dialogar con el Infectado.":
            jump ruta_c2_dialogar

        "No hacer nada.":
            jump ruta_c2_b


# ============================================================
# RUTA C1 - INTENTAR CORRER
# ============================================================

label ruta_c1_correr:

    show mc aterrado_2

    "Con las pocas fuerzas que me quedaban, corrí hacia la puerta que tenía enfrente."

    "No miré hacia otro lado."

    "No me importaba el horror ni la fatiga que me hacía arrodillar."

    "No me importaba NADA."

    "Solo quería alejarme de lo que sea que estaba viéndome."

    "Un cansancio tan extremo me estaba atormentando."

    "Detrás de mí, la voz de la criatura comenzó a elevarse."

    infectado1 "¡Buenos días!"

    infectado1 "¡Uno de chocolate, por favor!"

    # TODO SFX: puerta cerrándose

    "Llegué a la puerta, la abrí y la azoté detrás de mí."


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    scene bg1
    show mc aterrado

    "Frente a mí se encontraba nuevamente el familiar puesto de helados."

    "El mostrador."

    "Las máquinas."

    "Los productos."

    "Todo parecía normal."

    "¿Demasiado normal?"

    "El aroma dulce característico del lugar no logró tranquilizarme en lo más mínimo."

    "Al contrario."

    "Me recordó lo poco lógico que es estar aquí."

    show mc colapso
    # TODO miedo("colapso")

    "El miedo inunda mi cuerpo una vez más."

    "Mi respiración se volvió aún más irregular."

    "La hiperventilación me impedía pensar correctamente."

    "Pasaron varios minutos."

    "Permanezco dentro del local intentando recuperar la calma."

    "{color=[thought_color]}\"Respira.\"{/color}"
    "{color=[thought_color]}\"Solo respira.\"{/color}"
    "{color=[thought_color]}\"No necesito entender ahora mismo qué está pasando.\"{/color}"
    "{color=[thought_color]}\"Solo necesito volver a mí.\"{/color}"

    # TODO SFX: vibración
    # TODO: Me gustaria hacer un tipo screamer del MC con el celular, que a todos nos a espantado una mmda
    # TODO BG: personalizado del MC horrorizado y usado para hacer un screamer basico tirado en el puesto de helados y el bote se basura con luz del celular

    show mc nervioso_2

    "Casi me cago del susto que me da un sonido."

    "Una vibración."

    "El celular que estaba dentro del bote de basura."

    "Decido ver dentro del bote de basura y ver por qué está vibrando."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE: celular con notificación
    $ asimilacion = 80

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2


# ============================================================
# RUTA C2 - DIALOGAR CON EL INFECTADO
# ============================================================

label ruta_c2_dialogar:

    show mc asustado

    "Me armo de valor y decido hablar con lo que tengo enfrente."

    "Nunca había sentido un miedo semejante de estar aquí."

    "Las palabras apenas lograban tener coherencia."

    show mc nervioso_2

    mc "B-buenas noches."

    mc "L-la gerente se ha ido más temprano."

    "El ambiente comenzó a romperse."

    "No físicamente."

    "O quizás sí."

    "Era imposible saberlo."

    "El sonido alrededor parecía distorsionarse."

    show mc aterrorizado
    # TODO miedo("aterrorizado")

    "Un horror aún más fuerte invadió cada fibra de mi ser."

    "La voz del Infectado respondió."

    infectado1 "Buenas noches."

    infectado1 "Es una pena."

    infectado1 "Favor de decir que la siguiente semana se..."


    # TODO EFFECT: distorsión fuerte de voz, se tiene que dar a entender que lo que tiene que ver con la siguiente semana
    # ES UN MISTERIO y no se puede decir, mencionar ni sugerir
    # Es como silenciar al infectado
    # TODO SFX: la voz pierde el sonido (silencio total unos segundos)


    "La voz se distorsionó completamente, las palabras perdieron su sonido y mis sentidos dejaron de estar conectados a mí."

    "Después volví a escuchar."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    "Permanezco completamente inmóvil y sin lograr pensar."

    "Desde mi visión periférica comienzo a divisar algo."

    "¿Un cuello?"

    "Recorriendo todo el centro de la plaza."

    "Atravesando paredes."

    "Desapareciendo dentro de estructuras."

    "Extendiéndose mucho más allá de lo que podía comprender y haciendo nudos por todos lados."

    "La cabeza del Infectado me observaba más fijamente."

    "{color=[thought_color]}\"¿Qué chingados es todo esto? NO QUIERO MORIR.\"{/color}"

    "La criatura inclinó ligeramente la cabeza."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    show mc aterrado_2

    "El miedo nubla mi juicio."

    # ========================================================
    # DECISIÓN POR TIEMPO
    # ========================================================

    # TODO: convertir este menú en una decisión con temporizador

    menu:

        "¿QUÉ HACER?"

        "Responder con la verdad.":
            jump ruta_c2_a

        "No hacer nada.":
            jump ruta_c2_b


# ============================================================
# RUTA C2-A - RESPONDER CON LA VERDAD
# ============================================================

label ruta_c2_a:

    show mc aterrado

    "Con todo y pánico que hay en cada parte de mi cuerpo, decido responder con la verdad."

    show mc nervioso_2

    mc "E-estaba buscando la salida."

    mc "S-solo que me tropecé un poco."

    "Trago saliva instintivamente."

    "Ni siquiera mi mente podía procesar lo que mi vista alcanzaba a ver."

    "Un miedo aún peor de intentar razonar lo que pasa me nubla más."

    "El Infectado permanece observándome."

    "Durante unos segundos más no dijo nada."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    "Si existiera algo que me pudiera poner peor, era eso."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    show mc colapso
    # TODO miedo("colapso")

    "El pánico aumentó tanto que mi cuerpo terminó colapsando."

    "Las palabras que escucho se distorsionan y resuenan dentro de mis oídos."


    # ========================================================
    # EFECTO DE DISTORSIÓN
    # ========================================================

    # TODO EFFECT: texto creciendo / distorsión

    show mc colapso_2

    "\"Quiero uno de chocolate sencillo, por favor.\""

    "\"Quiero uno de chocolate sencillo, por favor.\""

    "\"QUIERO UNO DE CHOCOLATE.\""

    "\"QUIERO DE CHOCOLATE.\""

    "\"CONO SENCILLO.\""

    # TODO EFFECT: texto ocupando toda la pantalla
    # TODO EFFECT: interfaz desapareciendo parcialmente
    # Tiene que transmitir un sentimiento de que fuiste abrumado por algo, para que puedan entender esto imagenen lo siguiente
    # En tu campo visual y todo lo que logras ver imagina una cara que abarca todo lo que ves, al razonar eso escuchas la misma cosa repitiendose
    # Si intentas tomar en serio ese ejemplo, te da un miedo existencial y eso busco transmitir aqui

    # TODO BG: corriendo del infectado 1 con el cuello por todos lados y la cabeza por arriba de la pantalla

    "La voz terminaría dejándome loco."

    "No aguanté más esta situación."

    "{color=[thought_color]}\"NO PUEDO SEGUIR AQUÍ.\"{/color}"

    "Decido correr hacia la salida."

    "Llego a la puerta, la abro y la azoto detrás de mí."


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    scene bg1
    show mc aterrado

    "Frente a mí se encontraba nuevamente el familiar puesto de helados."

    "El mostrador."

    "Las máquinas."

    "Los productos."

    "Todo parecía normal."

    "¿Demasiado normal?"

    "Aunque con tanto miedo ni siquiera logro analizar que estoy en la tienda de helados y no en la salida de la plaza."

    "Mi respiración se volvió aún más irregular."

    "La hiperventilación me impedía pensar correctamente."

    "Pasaron varios minutos."

    "Permanezco dentro del local intentando recuperar la calma."

    "{color=[thought_color]}\"Respira.\"{/color}"
    "{color=[thought_color]}\"Solo respira.\"{/color}"
    "{color=[thought_color]}\"No entiendo qué era, no entiendo qué hago aquí, no entiendo por qué intento entender.\"{/color}"
    "{color=[thought_color]}\"Solo necesito volver a mí.\"{/color}"

    # TODO SFX: vibración
    # TODO: Me gustaria hacer un tipo screamer del MC con el celular, que a todos nos a espantado una mmda
    # TODO BG: personalizado del MC horrorizado y usado para hacer un screamer basico tirado en el puesto de helados y el bote se basura con luz del celular

    show mc nervioso_2

    "Casi me cago del susto que me da un sonido."

    "Una vibración."

    "El celular que estaba dentro del bote de basura."

    "Decido ver dentro del bote de basura y ver por qué está vibrando."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # TODO IMAGE: celular con notificación
    $ asimilacion = 80

    "{b}ASIMILACIÓN: [asimilacion]%%{/b}"

    # FIN DE ESTA RUTA: pasa al capitulo 2 (capitulos/capitulo_2/cap2_inicio.rpy)

    jump capitulo_2


# ============================================================
# RUTA C2-B - NO HACER NADA
# ============================================================

label ruta_c2_b:

    # TODO BG: plaza oscura
    # TODO SPRITE: Infectado 1

    show mc nervioso_2

    "No respondo."

    "No hago ningún movimiento."

    "Permanezco completamente inmóvil."

    "..."

    show mc asustado
    # TODO miedo("asustado")

    "Mi capacidad de pensamiento comienza a fallar."

    "La criatura continuaba observándome."

    infectado1 "¿Te encuentras bien?"

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

