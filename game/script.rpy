
# Alchile que organicen bien el codigo porque si hacemos un asco l o s m a t o - Chinjas


#### Ahora mismo no esta completo esto, es jugable al menos en texto pero me pondre a trabajar en: 
#### no.1 Mis dialogos los re hare todos uno por uno porque esta bien pinche robotico todo
#### no.2 Hay dialogos extras que no eran, los voy a borrar y hacer legible
#### Revisen donde dice RECURSOS ahi esta puesto las rutas de las imagenes y del fondo, el script y si hago otro en el futuro seran puro codigo de la historia
#### si necesitan definir algo o por ejemplo el codigo del algoritmo haganlo en otro archivo, el inventario lo usaremos en el capitulo 2 de esta demo
#### no.3 me falta los efectos de sonido y imagenes, hare luego una lista con las imagenes especificas
#### la neta que no tengo ahora mismo cerebro porque tengo sueño pero mañana hago esto mas ordenado como dije o si leen esto mañana pos cuando esto este eliminado es q ya lo complete
#### La logica matematica lo hare cuando termine esto, porque si continuo la historia al final no usare la IA de los infectados que sera una parte esencial del juego final
#### Att. Chinjas




# ============================================================
# CAPÍTULO 1 - Desiciones del jugador con la asimlacion
 ============================================================

label start:

    scene bg1

    "La noche había caído."

    "Sin explicación alguna, la plaza quedó sumida en un silencio sepulcral."

    "Una oscuridad extraña había invadido gran parte del lugar."
    "Pocas luces continuaban funcionando, parpadeando de manera intermitente."

    show mc_pensante

    "El MC dejó de caminar."

    $ thought_color = "#8ecae6"

    "{color=[thought_color]}\"Yo sé que esto no es normal.\"{/color}"
    "{color=[thought_color]}\"Lo sé.\"{/color}"
    "{color=[thought_color]}\"Y sé que incluso ella tampoco lo es.\"{/color}"

    "El MC decidió mirar a su alrededor."

    "Ni siquiera un apagón debería hacer que un lugar se sintiera así."

    "{color=[thought_color]}\"Esto da maldito miedo.\"{/color}"
    "{color=[thought_color]}\"Tengo que salir de aquí. No necesito nada más.\"{/color}"

    "El MC regresó rápidamente hacia el puesto de helados."

    scene bg2

    "Al entrar nuevamente a la tienda, algo llamó su atención."

    "Sobre el mostrador continuaba el celular antiguo que el cliente había olvidado."

    "El mismo teléfono que nadie parecía reclamar."

    "El MC permaneció observándolo durante unos segundos."

    "Había algo extraño en él."

    "No sabía exactamente qué."

    "Pero tampoco podía ignorar la sensación de que ese objeto no debería estar ahí."

    "{color=[thought_color]}\"¿Por qué sigue aquí?\"{/color}"
    "{color=[thought_color]}\"¿Y por qué nadie ha venido a buscarlo?\"{/color}"

    "El MC se acercó lentamente al mostrador."

    scene bgcelular

    menu:

        "¿QUÉ HACER CON EL CELULAR?"

        "Tomarlo.":
            jump tomar_celular

        "Dejarlo donde está.":
            jump dejar_celular

        "Tirarlo a la basura.":
            jump tirar_celular


# ============================================================
# RUTA A - TOMAR EL CELULAR
# ============================================================

label tomar_celular:

    # SPRITE: MC tomando el celular
    # BG: mostrador de la tienda

    "El MC tomó el teléfono."

    "{color=[thought_color]}\"Probablemente tenga algún uso.\"{/color}"
    "{color=[thought_color]}\"Será mejor tener esto que no tener nada.\"{/color}"

    "Observó el dispositivo durante unos segundos."

    "{color=[thought_color]}\"Es demasiado raro que todavía no encuentre el mío.\"{/color}"
    "{color=[thought_color]}\"Ni siquiera sé dónde podría estar.\"{/color}"

    # SFX: vibración del celular

    "De repente, el teléfono vibró."

    # SPRITE: MC sorprendido / alerta

    "El MC se quedó inmóvil."

    "{color=[thought_color]}\"...¿Qué?\"{/color}"

    "Observó la pantalla."

    "No había ninguna notificación visible."

    "Tampoco parecía tener señal."

    # SFX: segunda vibración

    "Entonces volvió a vibrar."

    "{color=[thought_color]}\"Esto no debería estar pasando.\"{/color}"

    "El MC guardó rápidamente el teléfono en su bolsillo."

    "{color=[thought_color]}\"Me voy.\"{/color}"
    "{color=[thought_color]}\"Ya tuve suficiente por hoy.\"{/color}"


    # ========================================================
    # SALIDA DE LA TIENDA
    # ========================================================

    # BG: plaza después del apagón

    "El MC caminó rápidamente hacia la salida ubicada al otro extremo de la plaza."

    "Cada paso se sentía más pesado que el anterior."

    "No sabía por qué."

    "Simplemente quería salir de ahí."

    # SFX: vibración del celular

    "El celular volvió a vibrar."

    "{color=[thought_color]}\"¿Qué se supone que le pasa a esto?\"{/color}"

    "El MC sacó el teléfono de su bolsillo."

    "Una notificación apareció en la pantalla."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE / EFECTO: pantalla del celular

    "{b}ASIMILACIÓN: 10%%{/b}"

    # SPRITE: MC confundido

    mc "¿Qué?"

    "El MC levantó lentamente la mirada."

    "Frente a él, a pocos metros de distancia, se encontraba la puerta de salida."

    "Sin embargo, algo se movía en medio de ella."

    "La poca luz que quedaba permitía distinguir una forma imposible."

    "Parecía una rueda de automóvil girando lentamente."

    "Un espiral."

    "Una masa retorcida que se estrangulaba sobre sí misma."

    "El movimiento no tenía sentido."

    "No parecía pertenecer a ninguna forma de vida conocida."

    "Tal vez un vórtice de carne sería la única manera de describirlo."

    # SPRITE: MC perturbado

    "El MC permaneció inmóvil."

    "{color=[thought_color]}\"No.\"{/color}"
    "{color=[thought_color]}\"No, no, no.\"{/color}"

    "La forma continuaba moviéndose."

    "El MC sintió que algo dentro de él reconocía aquella presencia."

    "Algo familiar."

    "O peor."

    "Algo que no quería volver a ver."

    # IMAGE: infectado bloqueando la salida
    # BG: salida de la plaza


    # ========================================================
    # LA PLAZA
    # ========================================================

    "El MC retrocedió rápidamente."

    "{color=[thought_color]}\"No voy a acercarme a eso.\"{/color}"
    "{color=[thought_color]}\"Ni de puta casualidad.\"{/color}"

    "Decidió regresar hacia el puesto de helados."

    "Sin embargo, algo había cambiado."

    # BG: diferentes pasillos de la plaza

    "Por los diferentes pasillos de la plaza comenzaron a aparecer masas en movimiento."

    "Una."

    "Dos."

    "Tres."

    "El MC miró hacia los distintos corredores."

    "No podía distinguir exactamente qué eran."

    "Todas se movían de una manera similar."

    "Retorciéndose."

    "Girando."

    "Desplazándose lentamente."

    # SPRITE: MC completamente espantado

    "El MC estaba completamente espantado."

    "Había visto algo."

    "Algo que no debería existir."

    "Y ahora no sabía si realmente estaba solo."

    "{color=[thought_color]}\"¿Qué carajo está pasando aquí?\"{/color}"

    # EFFECT: ligera distorsión de pantalla
    # SFX: vibración del celular

    "El teléfono volvió a vibrar."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B - DEJAR EL CELULAR
# ============================================================

label dejar_celular:

    # SPRITE: MC observando el celular
    # BG: mostrador

    "El MC observó el teléfono durante unos segundos más."

    "Después apartó la mirada."

    mc "Y una mierda."

    "Decidió no tocarlo."

    "No quería involucrarse con algo que claramente no comprendía."

    "{color=[thought_color]}\"Seguro alguien va a venir por él.\"{/color}"
    "{color=[thought_color]}\"Y si no, tampoco es mi problema.\"{/color}"

    "El MC salió rápidamente de la tienda."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # BG: plaza después del apagón

    "El MC caminó hacia la salida al otro extremo de la plaza."

    "Cada paso se sentía pesado y cansado."

    "Sin embargo, todavía era una sensación tolerable."

    "Podía caminar."

    "Podía pensar."

    "Por el momento."

    # EFFECT: luces parpadeando

    "Las luces comenzaron a parpadear con mayor frecuencia."

    "{color=[thought_color]}\"Aunque no me hubiera venido mal intentar llamar con ese celular.\"{/color}"

    "El MC continuó caminando."

    "Entonces ocurrió."

    # SFX: apagón

    "Todas las luces de la plaza se apagaron al mismo tiempo."

    "Un apagón absoluto."

    mc "Mierda."

    mc "Lo que faltaba."

    "Durante unos segundos no pudo ver absolutamente nada."

    # SFX: sonido de masa retorciéndose

    "Entonces escuchó un sonido."

    "Algo parecido a nudos retorciéndose."

    "Como si una masa enorme se moviera lentamente en la oscuridad."

    "El sonido provenía de algún lugar cercano."

    "Muy cercano."


    # ========================================================
    # EL INFECTADO 1
    # ========================================================

    # SPRITE: INFECTADO 1
    # BG: plaza completamente oscura
    # EFFECT: pantalla oscura

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "El MC se sobresaltó."

    mc "Buenas noches."

    mc "Estaba buscando la salida."

    mc "Me quedé hasta tarde."

    "Era incómodo."

    "Extremadamente incómodo."

    "Hablar con alguien en medio de una plaza completamente a oscuras."

    "Pero había algo más."

    "La voz parecía incorrecta."

    "No por lo que decía."

    "Sino por cómo lo decía."

    infectado1 "Buenas noches."

    infectado1 "¿Usted de dónde trabaja?"

    infectado1 "Esta tienda debió cerrar hace tiempo."

    infectado1 "Desde que se quedó hasta tarde."

    "El silencio que siguió fue aún más incómodo."

    "El MC intentó mantener la calma."

    mc "Trabajo en el puesto de helados de aquí atrás."

    mc "¿Tendrá una lámpara?"

    "La voz permaneció en silencio durante unos segundos."

    # EFFECT: distorsión de voz

    infectado1 "Buenas noches..."

    infectado1 "Buenas noches..."

    infectado1 "En este lugar es tarde para que se encuentre..."

    infectado1 "¿Por qué no encuentra uno de chocolate?"

    "El MC permaneció inmóvil."

    "Las palabras no tenían sentido."

    "Pero una parte de él comenzaba a comprender algo."

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

    "El MC decidió regresar."

    "Sin pensarlo dos veces, comenzó a caminar en dirección al puesto de helados."

    "No quería seguir ahí."

    "No quería escuchar más aquella voz."

    "La memoria muscular funcionó antes que el pensamiento."

    "Sus piernas comenzaron a moverse rápidamente."

    # SFX: masa retorciéndose, aumentando

    "Mientras avanzaba, el sonido de la masa retorciéndose aumentó."

    "Un poco más fuerte."

    "Un poco más cerca."

    "Un poco más arriba."

    "Hasta que el MC comprendió que aquello no estaba lejos."

    "Estaba siguiéndolo."

    infectado1 "Buenos días."

    infectado1 "¿Uno de chocolate con su gente?"

    infectado1 "¿Por qué es tarde?"

    "El MC aceleró el paso."

    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"Solo sigue caminando.\"{/color}"

    "Finalmente llegó a la tienda."

    # SFX: puerta cerrándose

    "Entró y cerró la puerta de golpe."

    "Permaneció apoyado contra ella, completamente agitado."

    "Su respiración era irregular."

    "Necesitaba unos segundos para recuperar el control."

    # SFX: vibración

    "Entonces escuchó algo."

    "Una vibración."

    "Provenía del interior del local."

    "El sonido venía del bote de basura."

    "El MC volteó lentamente."

    # SPRITE: MC perturbado
    # IMAGE: bote de basura / celular

    "El celular estaba vibrando dentro de la basura."

    "{color=[thought_color]}\"...Yo no lo puse ahí.\"{/color}"


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 50%%{/b}"

    "El MC observó la pantalla."

    "No había tocado el teléfono."

    "No lo había tomado."

    "Ni siquiera sabía cómo había terminado dentro del bote de basura."

    # SFX: vibración continua

    "La vibración continuó."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2 - CONTINUAR DIALOGANDO CON LA VOZ
# ============================================================

label ruta_b2_dialogar:

    "El MC decidió no moverse."

    "No porque quisiera quedarse."

    "Sino porque no sabía qué otra cosa hacer."

    mc "¿Disculpe?"

    "La voz permaneció en silencio."

    "El sonido de algo retorciéndose continuaba alrededor."

    infectado1 "Buenas noches."

    mc "¿Usted sabe dónde está la salida?"

    "Silencio."

    mc "¿Se encuentra bien?"

    "La voz comenzó a responder lentamente."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "{color=[thought_color]}\"Está repitiendo lo mismo.\"{/color}"
    "{color=[thought_color]}\"¿Por qué?\"{/color}"

    infectado1 "¿Usted trabaja aquí?"

    mc "Sí."

    mc "En la tienda de helados."

    infectado1 "¿Uno de chocolate?"

    "El MC tragó saliva."

    mc "No."

    mc "Bueno..."

    mc "Hoy ya cerramos."

    "La voz permaneció en silencio."

    # SFX: golpe suave contra una pared

    "Entonces algo golpeó suavemente una pared cercana."

    mc "¿Señora?"

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    "Las palabras comenzaron a repetirse."

    "Cada vez más rápido."

    "Cada vez menos humanas."

    # EFFECT: distorsión

    "{color=[thought_color]}\"No quiero seguir hablando.\"{/color}"
    "{color=[thought_color]}\"Pero tampoco quiero darle la espalda.\"{/color}"


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

    "El MC decidió regresar."

    "Sin pensarlo demasiado, comenzó a caminar hacia el puesto de helados."

    "La voz continuaba detrás de él."

    infectado1 "Buenas noches."

    infectado1 "¿Uno de chocolate?"

    infectado1 "Buenas noches."

    # SFX: masa retorciéndose aumentando

    "El sonido de la masa retorciéndose aumentó."

    "El MC comenzó a caminar más rápido."

    "Después a correr."

    "No quería escuchar nada más."

    "Al llegar a la tienda, cerró la puerta de golpe."

    "Permaneció inmóvil durante unos segundos."

    # SFX: vibración

    "Entonces escuchó una vibración."

    "El celular estaba dentro del bote de basura."

    "El MC se acercó lentamente."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 50%%{/b}"

    "El MC observó el teléfono."

    "No entendía cómo había llegado ahí."

    "La pantalla mostraba una notificación nueva."

    "{b}ASIMILACIÓN: 50%{/b}"

    "{color=[thought_color]}\"¿Qué significa esto?\"{/color}"
    "{color=[thought_color]}\"¿Por qué está aumentando?\"{/color}"

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2-B - CONTINUAR DIALOGANDO
# ============================================================

label ruta_b2_b:

    "El MC permaneció frente a la oscuridad."

    "Intentó mantener la voz estable."

    mc "¿Usted trabaja aquí?"

    "La criatura no respondió inmediatamente."

    infectado1 "Buenas noches."

    mc "¿Qué está haciendo en esta plaza?"

    "Silencio."

    mc "¿Me está escuchando?"

    "El sonido alrededor comenzó a hacerse más fuerte."

    "Como si algo enorme se estuviera moviendo detrás de las paredes."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "{color=[thought_color]}\"Esto no tiene sentido.\"{/color}"
    "{color=[thought_color]}\"¿Por qué sigue diciendo lo mismo?\"{/color}"

    "El MC miró hacia la oscuridad."

    mc "¿Quiere uno de chocolate?"

    "La voz se detuvo."

    "Por primera vez."

    "Silencio absoluto."

    "Después respondió."

    infectado1 "Buenas noches."

    infectado1 "Uno de chocolate."

    # EFFECT: distorsión de voz

    infectado1 "Uno de chocolate."

    infectado1 "Uno de chocolate."

    infectado1 "UNO DE CHOCOLATE."

    "El MC sintió que algo estaba mal."

    "No sabía exactamente qué."

    "Pero comprendió que había cometido un error."

    "{color=[thought_color]}\"No debí decir eso.\"{/color}"

    "La oscuridad frente a él comenzó a moverse."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2-C - NO HACER NADA
# ============================================================

label ruta_b2_c:

    # BG: plaza oscura
    # SPRITE: Infectado 1

    "El MC no respondió."

    "No hizo ningún movimiento."

    "Permaneció completamente inmóvil."

    "..."

    "Su capacidad de pensamiento comenzó a deteriorarse."

    "Se sentía mareado."

    "Confundido."

    "Como si su cuerpo ya no respondiera correctamente."

    "..."

    "La criatura continuaba observándolo."

    infectado1 "¿Se encuentra bien?"

    "El MC no respondió."

    infectado1 "¿Necesita ayuda?"

    "..."

    "El sonido de la plaza comenzó a desaparecer."

    "Ya no podía escuchar las luces."

    "Ya no podía escuchar sus propios pasos."

    "Solo escuchaba la voz."

    "..."

    # EFFECT: distorsión progresiva
    # EFFECT: errores visuales

    "La imagen comenzó a distorsionarse."

    "Los sonidos del ambiente se volvieron irreconocibles."

    "La pantalla comenzó a presentar errores visuales."

    "Entonces apareció un mensaje."

    # IMAGE: mensaje en pantalla

    "\"¿Quién eres tú?\""

    "..."

    "\"Creo que puedo verte.\""

    "..."

    "\"Tal vez algún día logre entrar ahí también.\""

    # IMAGE: Infectado ocupando pantalla

    jump final_1_asimilacion


# ============================================================
# RUTA C - TIRAR EL CELULAR
# ============================================================

label tirar_celular:

    # SPRITE: MC tomando celular
    # BG: mostrador

    "El MC tomó el teléfono."

    "Sin pensarlo demasiado, lo arrojó dentro del bote de basura."

    "Permaneció observándolo durante un instante."

    "{color=[thought_color]}\"No es lo mismo dejarlo donde estaba que tirarlo a la basura.\"{/color}"
    "{color=[thought_color]}\"...¿Verdad?\"{/color}"

    "El MC comenzó a caminar hacia la salida."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # BG: plaza después del apagón

    "El MC salió rápidamente de la tienda."

    "Cada paso se sentía más pesado que el anterior."

    "No era cansancio."

    "No exactamente."

    "Era como si algo estuviera tirando de su cuerpo."

    "{color=[thought_color]}\"¿Qué está pasando?\"{/color}"

    "El peso aumentó repentinamente."

    "El MC perdió el equilibrio."

    "Sus piernas cedieron."

    "Cayó de rodillas sobre el suelo."

    "Durante unos segundos no pudo moverse."

    mc "¿Qué...?"

    "Intentó levantarse."

    "No pudo."

    # SFX: masa triturándose

    "Entonces escuchó un sonido."

    "Un movimiento parecido al de una masa triturándose."

    "No muy lejos de donde se encontraba."

    "El miedo recorrió todo su cuerpo."

    "El MC levantó lentamente la mirada."


    # ========================================================
    # EL INFECTADO 1 APARECE
    # ========================================================

    # SPRITE: INFECTADO 1
    # BG: plaza / criatura frente al MC
    # EFFECT: cuello extendiéndose

    "Una enorme cara se encontraba suspendida sobre él."

    "No tenía pupilas."

    "No parecía tener una expresión humana."

    "Su cuello se extendía por todo el pasillo."

    "Giraba sobre sí mismo."

    "Se expandía."

    "Desaparecía dentro de las paredes."

    "Volvía a aparecer más lejos."

    "Era imposible comprender cómo podía existir una estructura semejante."

    "El MC sintió que algo dentro de él comenzaba a romperse."

    "El horror recorrió su cuerpo."

    "Entonces la criatura habló."

    infectado1 "Buenas tardes."

    infectado1 "¿Estará la gerente?"

    infectado1 "Quiero hablar sobre los horarios de apertura para la siguiente semana."

    "El MC no podía procesar lo que estaba escuchando."

    "La criatura estaba frente a él."

    "Algo completamente imposible."

    "Y estaba hablando sobre horarios laborales."

    "{color=[thought_color]}\"¿Qué mierda?\"{/color}"
    "{color=[thought_color]}\"¿Qué estoy viendo?\"{/color}"
    "{color=[thought_color]}\"¿Por qué está hablando como si esto fuera normal?\"{/color}"

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

    "Con las pocas fuerzas que le quedaban, el MC corrió hacia la puerta que tenía enfrente."

    "No miró hacia otro lado."

    "No le importaba el dolor."

    "No le importaba nada."

    "Solo quería alejarse de aquella presencia."

    "La respiración del MC se volvió desesperada."

    "Detrás de él, la voz del Infectado comenzó a elevarse."

    infectado1 "¡Buenos días!"

    infectado1 "¡Uno de chocolate, por favor!"

    "El MC llegó hasta la puerta."

    # SFX: puerta abriéndose

    "La abrió."

    "Entró."

    # SFX: puerta cerrándose

    "Y la cerró inmediatamente."


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    # BG: tienda de helados
    # SPRITE: MC agitado

    "Frente a él se encontraba nuevamente el familiar puesto de helados."

    "El mostrador."

    "Las máquinas."

    "Los productos."

    "Todo parecía normal."

    "Demasiado normal."

    "El aroma dulce característico del lugar no logró tranquilizarlo."

    "Al contrario."

    "Le recordó lo peor."

    "El miedo inundó su cuerpo."

    "Su respiración se volvió irregular."

    "La hiperventilación le impedía pensar correctamente."

    "Pasaron varios minutos."

    "El MC permaneció dentro del local intentando recuperar la calma."

    "{color=[thought_color]}\"Respira.\"{/color}"
    "{color=[thought_color]}\"Solo respira.\"{/color}"
    "{color=[thought_color]}\"No estás viendo nada.\"{/color}"
    "{color=[thought_color]}\"Solo fue una mala noche.\"{/color}"

    # SFX: vibración

    "Entonces escuchó un sonido."

    "Una vibración."

    "El celular estaba dentro del bote de basura."

    "El MC levantó lentamente la mirada."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 80%%{/b}"

    mc "No..."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA C2 - DIALOGAR CON EL INFECTADO
# ============================================================

label ruta_c2_dialogar:

    "El MC intentó hablar."

    "Nunca había sentido un miedo semejante."

    "Las palabras apenas lograban salir de su boca."

    mc "B-buenas noches."

    mc "L-la gerente se ha ido más temprano."

    "El ambiente comenzó a retorcerse."

    "No físicamente."

    "O quizás sí."

    "Era imposible saberlo."

    "El sonido alrededor parecía distorsionarse."

    "La voz del Infectado respondió."

    infectado1 "Buenas noches."

    infectado1 "Es una pena."

    infectado1 "Favor de decir que la siguiente semana se..."

    "La frase se interrumpió."

    # EFFECT: distorsión fuerte de voz

    "La voz se distorsionó completamente."

    "Las palabras perdieron su forma."

    "Después volvió a hablar."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    "El MC permaneció inmóvil."

    "Desde su visión periférica comenzó a observar algo."

    "Un cuello."

    "Recorriendo todo el centro de la plaza."

    "Atravesando paredes."

    "Desapareciendo dentro de estructuras."

    "Extendiéndose mucho más allá de lo que podía comprender."

    "La cabeza del Infectado lo observaba fijamente."

    "{color=[thought_color]}\"No puede ser.\"{/color}"
    "{color=[thought_color]}\"Eso no cabe aquí.\"{/color}"
    "{color=[thought_color]}\"¿Cómo puede estar ahí?\"{/color}"

    "La criatura inclinó ligeramente la cabeza."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    "El MC no respondió."

    "La criatura esperó."


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

    "Con el miedo aún peor que antes, el MC logró responder."

    mc "E-estaba buscando la salida."

    mc "S-solo que me tropecé un poco."

    "Tragó saliva instintivamente."

    "No podía comprender qué estaba ocurriendo."

    "No podía encontrar una explicación lógica."

    "El Infectado permaneció observándolo."

    "Durante unos segundos no dijo nada."

    "Después habló."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    "El MC permaneció inmóvil."

    "La criatura repitió la frase."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    "El pánico aumentó."

    "Las palabras comenzaron a distorsionarse."


    # ========================================================
    # EFECTO DE DISTORSIÓN
    # ========================================================

    # EFFECT: texto creciendo / distorsión

    "\"Quiero uno de chocolate sencillo, por favor.\""

    "\"Quiero uno de chocolate sencillo, por favor.\""

    "\"QUIERO UNO DE CHOCOLATE.\""

    "\"QUIERO DE CHOCOLATE.\""

    "\"CONO SENCILLO.\""

    # EFFECT: texto ocupando toda la pantalla
    # EFFECT: interfaz desapareciendo parcialmente

    "La voz dejó de sonar humana."

    "El MC ya no podía permanecer ahí."

    "{color=[thought_color]}\"No.\"{/color}"
    "{color=[thought_color]}\"No puedo seguir aquí.\"{/color}"

    "Decidió correr hacia la salida."

    # SFX: puerta

    "Abrió la puerta."

    "Y la cerró rápidamente detrás de él."


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    # BG: tienda de helados
    # SPRITE: MC perturbado

    "Frente a él estaba nuevamente el puesto de helados."

    "El mismo lugar."

    "El mismo aroma dulce."

    "El mismo mostrador."

    "Pero algo había cambiado."

    "El miedo extremo inundó su cuerpo."

    "Su respiración se volvió irregular."

    "Pasaron varios minutos."

    "Entonces escuchó una vibración."

    "El celular continuaba dentro del bote de basura."

    "El MC se acercó lentamente."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 70%%{/b}"

    "{color=[thought_color]}\"¿Por qué sigue aquí?\"{/color}"
    "{color=[thought_color]}\"¿Por qué sigue aumentando?\"{/color}"

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA C2-B - NO HACER NADA
# ============================================================

label ruta_c2_b:

    # BG: plaza oscura
    # SPRITE: Infectado 1

    "El MC no respondió."

    "No hizo ningún movimiento."

    "Permaneció completamente inmóvil."

    "..."

    "Su capacidad de pensamiento comenzó a deteriorarse."

    "Se sentía mareado."

    "Confundido."

    "Como si su cuerpo ya no respondiera correctamente."

    "..."

    "La criatura continuaba observándolo."

    infectado1 "¿Se encuentra bien?"

    "El MC no respondió."

    infectado1 "¿Necesita ayuda?"

    "..."

    "El sonido de la plaza comenzó a desaparecer."

    "Ya no podía escuchar las luces."

    "Ya no podía escuchar sus propios pasos."

    "Solo escuchaba la voz."

    "..."

    # EFFECT: distorsión progresiva
    # EFFECT: errores visuales

    "La imagen comenzó a distorsionarse."

    "Los sonidos del ambiente se volvieron irreconocibles."

    "La pantalla comenzó a presentar errores visuales."

    "Entonces apareció un mensaje."

    # IMAGE: mensaje en pantalla

    "\"¿Quién eres tú?\""

    "..."

    "\"Creo que puedo verte.\""

    "..."

    "\"Tal vez algún día logre entrar ahí también.\""

    # IMAGE: Infectado ocupando pantalla

    jump final_1_asimilacion


# ============================================================
# FINAL 1 - ASIMILACIÓN
# ============================================================

label final_1_asimilacion:

    # IMAGE: INFECTADO 1 ocupando toda la pantalla
    # EFFECT: interfaz oculta
    # EFFECT: zoom lento
    # SFX: ambiente distorsionado

    "El jugador observa directamente al Infectado."

    "La criatura parece estar mirando más allá del personaje."

    "Parece mirar al jugador."

    

    # EFFECT: zoom lento
    # EFFECT: distorsión progresiva
    # SFX: voces repetidas


    # ========================================================
    # MECÁNICA ESPECIAL DEL FINAL
    # ========================================================

    # TODO:
    # Al cerrar y volver a abrir el juego, el jugador deberá
    # regresar directamente a este final.
    #
    # TODO:
    # Implementar combinación específica de botones para
    # reiniciar la demo.
    #
    # Hasta que se descubra la combinación, esta escena
    # deberá permanecer activa.

    while True:
        pause

