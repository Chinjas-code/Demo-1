
# Alchile que organicen bien el codigo porque si hacemos un asco l o s m a t o - Chinjas


#### ACTUALIZACION del dia 16/09/26
#### Raza ya me lei todos los dialogos y segun yo ya deje todos legibles borre las cosas extra y las puse con mas sentido y menos robotico, no creo haber señalado bien
#### todas las cosas que debemos poner como bg o como cosas como las imagenes de los personajes ya conforme vaya haciendo esto y poniendo tambien efectos de sonido
#### los ire poniendo bien bien, ahora mismo lo que se tiene que hacer es ir poniendo bien el juego y el juego si funciona ahora mismo como esta solamente hay que poner que 
#### se vea bien y por lo mientras tendriamos algo medio jugable

#### Texto anterior importante:
#### Ahora mismo no esta completo esto, es jugable al menos en texto 
#### Revisen donde dice RECURSOS ahi esta puesto las rutas de las imagenes y del fondo, el script y si hago otro en el futuro seran puro codigo de la historia
#### si necesitan definir algo o por ejemplo el codigo del algoritmo haganlo en otro archivo, el inventario lo usaremos en el capitulo 2 de esta demo


# ============================================================
# CAPÍTULO 1 - Desiciones del jugador con la asimlacion
#============================================================

label start:

    scene bg1

    "La noche había caído."

    "Sin explicación alguna, la plaza quedó sumida en un silencio sepulcral."

    "Una oscuridad extraña había invadido gran parte del lugar."
    "Pocas luces continuaban funcionando, parpadeando de manera intermitente."

    show mc_pensante

    "El MC dejó de caminar."

    $ thought_color = "#8ecae6"

    "{color=[thought_color]}\"Yo sé que esta situación no es normal.\"{/color}"
    "{color=[thought_color]}\"Lo sé muy bien.\"{/color}"
    "{color=[thought_color]}\"Y sé que incluso ella tampoco lo es.\"{/color}"
    "{color=[thought_color]}\"No tiene ningún sentido la forma que interactua conmigo cuando pide helados.\"{/color}"

    "El MC decidió mirar a su alrededor."

    "Ni siquiera un apagón debería hacer que un lugar se sintiera así de abrumador, era una un ambiente muy pesado."

    "{color=[thought_color]}\"Esto da maldito miedo.\"{/color}"
    "{color=[thought_color]}\"Tengo que salir de aquí. No quiero ver como todo se desaparece de nuevo.\"{/color}"

    "Decides regresar rápidamente hacia el puesto de helados por tus cosas."

    scene bg2

    "Al entrar nuevamente a la tienda, algo llamó tu atención."

    "Sobre el mostrador continuaba el celular antiguo que un cliente había olvidado."

    "El mismo teléfono que nadie parecía reclamar, bastante extraño."

    "Permaneces observándolo durante unos segundos."

    "No sabía exactamente para que pero te podria resultar util."

    "{color=[thought_color]}\"¿Por qué sigue aquí?\"{/color}"
    "{color=[thought_color]}\"¿Y por qué nadie ha venido a buscarlo? Aunque tampoco me extraña viendo lo feo que es\"{/color}"

    "Te acercas lentamente al mostrador."

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
    # BG: mostrador de la tienda creo que seria el bg2

    "Tomas el teléfono."

    "{color=[thought_color]}\"Probablemente tenga algún uso.\"{/color}"
    "{color=[thought_color]}\"Será mejor tener esto que no tener nada.\"{/color}"

    "Observaste el dispositivo durante unos segundos."

    "{color=[thought_color]}\"Es demasiado raro que todavía no encuentre el mío.\"{/color}"
    "{color=[thought_color]}\"Ni siquiera sé dónde podría estar, tal vez la gerente realmente se lo llevo.\"{/color}"

    # SFX: vibración del celular

    "De repente, el teléfono vibró."

    # SPRITE: MC sorprendido / alerta

    "Te quedas inmóvil."

    "{color=[thought_color]}\"...¿Qué?\"{/color}"

    "Observaste la pantalla."

    "No había ninguna notificación visible."

    "Tampoco parecía tener señal."

    # SFX: segunda vibración

    "Entonces volvió a vibrar."

    # SPRITE: MC cansado / alerta

    "{color=[thought_color]}\"Mierda, cualquier cosa ya me asusta.\"{/color}"

    "Te guardas rápidamente el teléfono en tu bolsillo."

    "{color=[thought_color]}\"Me voy.\"{/color}"
    "{color=[thought_color]}\"Ya tuve suficiente por este turno.\"{/color}"


    # ========================================================
    # SALIDA DE LA TIENDA
    # ========================================================

    # BG: plaza después del apagón, un pasillo

    "Te dirigiste rápidamente hacia la salida ubicada al otro extremo de la plaza."

    "Cada paso se sentía más pesado que el anterior."

    "No sabía por qué, el cansancio debe estar afectandote."

    # SFX: vibración del celular

    "El celular volvió a vibrar."

    "{color=[thought_color]}\"¿Qué se supone que le pasa a esto?\"{/color}"

    "Te sacaste el teléfono de tu bolsillo."

    "Una notificación apareció en la pantalla."
    
    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE / EFECTO: pantalla del celular

    "{b}ASIMILACIÓN: 10%%{/b}"

    # SPRITE: MC confundido

    mc "¿Qué?"

    "Te levantaste lentamente la mirada."

    "Frente a ti, a pocos metros de distancia, se encontraba la puerta de salida."

    "Sin embargo, algo se movía en medio de alrededor tuyo."

    "La poca luz que quedaba permitía distinguir algo que no logras entender."

    #TODO Aqui quisiera intentar un efecto donde se quita el fondo que este ahora mismo puesto como un parpadeo ya que siento que podria ser util,
    # Basicamente seria como una transicion digamos que en bg1 esta todo normal pero se parpadea y ahora sale el infectado con efecto de estatica en ese mismo BG

    #BG de pasillo con infectado con efecto de distorsion y estatica, si se puede
    #ya veremos si sabemos animar los bg
    "Parecía una rueda de automóvil girando lentamente y retorciendose."

    "Un espiral."

    "Una masa retorcida que se estrangulaba sobre sí misma para avanzar."

    "El movimiento no tenía sentido."

    "Tal vez un vórtice de carne sería la única manera de describirlo."

    # SPRITE: MC perturbado

    "Permaneciste inmóvil ante semejante vista."

    "{color=[thought_color]}\"No.\"{/color}"
    "{color=[thought_color]}\"No, no, no.\"{/color}"

    "La forma continuaba moviéndose hacia ti."

    "Te sentiste que algo dentro de ti reconocía aquella presencia como alguien que llegaste a ver."

    # IMAGE: infectado bloqueando la salida
    # BG: salida de la plaza


    # ========================================================
    # LA PLAZA
    # ========================================================

    "Te retrocediste rápidamente."

    "{color=[thought_color]}\"No voy a acercarme a eso.\"{/color}"
    "{color=[thought_color]}\"Ni de puta casualidad.\"{/color}"

    "Decidiste regresar hacia el puesto de helados."

    "Sin embargo, algo había cambiado."

    # BG: diferentes pasillos de la plaza

    "Por los diferentes pasillos de la plaza comenzaron a aparecer masas en movimiento."

    "Una."

    "Dos."

    "Tres."

    "Miraste hacia los distintos corredores."

    "No podía distinguir exactamente qué eran."

    "Todas se movían de una manera similar."

    "Retorciéndose."

    "Girando."

    "Desplazándose lentamente por todos lados."

    # SPRITE: MC completamente espantado

    "Estabas completamente espantado."

    "Sin comprension de tu alrededor."

    "{color=[thought_color]}\"¿Que mierda esta pasando?\"{/color}"

    # EFFECT: ligera distorsión de pantalla
    #BG de puesto de helados

    "terminaste llegando a tu puesto de helados y rapidamente cerraste la puerta."

    # SFX: vibración del celular

    "El teléfono volvió a vibrar."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B - DEJAR EL CELULAR
# ============================================================

label dejar_celular:

    # SPRITE: MC Neutral
    # BG: mostrador con celular

    "Observaste el teléfono durante unos segundos más."

    "Después apartó la mirada."

    "{color=[thought_color]}\"Mejor no tocar esa mierda.\"{/color}"

    "Decidiste no tocarlo."

    "{color=[thought_color]}\"Seguro alguien va a venir por él.\"{/color}"
    "{color=[thought_color]}\"Y si no, supongo al rato puedo hacer algo mas.\"{/color}"

    "Sales rápidamente de la tienda."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # BG: plaza después del apagón

    "Caminaste hacia la salida al otro extremo de la plaza."

    "Cada paso se sentía pesado y cansado."

    # EFFECT: luces parpadeando

    "Las luces comenzaron a parpadear con mayor frecuencia."

    #MC pensandte

    "{color=[thought_color]}\"Aunque no me hubiera venido mal intentar llamar con ese celular.\"{/color}"

    # SFX: apagón
    #Efecto de parpadeo 

    "Todas las luces de la plaza se apagaron al mismo tiempo."

    mc "Mierda."

    mc "Lo que faltaba."

    "Durante unos segundos no pudo ver absolutamente nada."

    # SFX: sonido de masa retorciéndose

    "Entonces escuchó un sonido de algo parecido a nudos retorciéndose."

    "Como si una masa enorme se moviera lentamente en la oscuridad."

    "El sonido provenía de algún lugar cercano."

    # ========================================================
    # EL INFECTADO 1
    # ========================================================

    # SPRITE: INFECTADO 1
    # BG: plaza completamente oscura con poca luz
    # EFFECT: pantalla oscura leve estatica

    #infectado 1 base no glitch

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "Te espanto"

    mc "Buenas noches."

    mc "Estaba buscando la salida."

    mc "Me quedé hasta tarde."

    "Era incómodo."

    "Extremadamente incómodo."

    "Hablar con alguien en medio de una plaza completamente a oscuras. ¿Que sentido tiene?"

    "Pero había algo más."

    infectado1 "Buenas noches."

    infectado1 "¿Usted de dónde trabaja?"

    infectado1 "Esta tienda debió cerrar hace tiempo."

    infectado1 "Desde que se quedó hasta tarde."

    "El silencio que siguió fue aún más incómodo."

    "El MC intentó mantener la calma."

    mc "Trabajo en el puesto de helados de aquí atrás."

    mc "¿Tendrá una lámpara?"

    "La voz permaneció en silencio durante unos segundos."

    # EFFECT: distorsión 
    #Infectado1 modiicado con cabeza alargada

    infectado1 "Buenas noches..."

    infectado1 "Buenas noches..."

    infectado1 "En este lugar es tarde para que se encuentre..."

    infectado1 "¿Por qué no encuentra uno de chocolate?"

    "Te quedas inmóvil."

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

    "Sin pensarlo dos veces, comienzas a caminar en dirección al puesto de helados."

    "No querías seguir ahí."

    "La memoria muscular funcionó antes que el pensamiento."

    "Tus piernas comenzaron a moverse rápidamente."

    # SFX: masa retorciéndose
    #BG de MC Huyendo de infectado 1 en medio de la plaza medio apagada, la cabeza debe estar por arriba con el cuello por todos lados

    "Mientras avanzabas, el sonido de la masa retorciéndose aumentó."

    "Un poco más fuerte y mas fuerte"

    "Te esta siguiendo"

    infectado1 "Buenos días."

    infectado1 "¿Uno de chocolate con su gente?"

    infectado1 "¿Por qué es tarde?"

    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"No voltees.\"{/color}"
    "{color=[thought_color]}\"Solo sigue corriendo.\"{/color}"

    "Finalmente llegas a la tienda."

    # SFX: puerta cerrándose
    #BG de tienda de helados con MC agitado

    "Entra y cierras la puerta de golpe."

    "Permanes apoyado contra ella recuperando el aliento aunque estas completamente agitado."

    # SFX: vibración

    mc "Una vibración?"

    "Provenía del interior del local."

    "El sonido venía del interior de la tienda."

    "El MC volteó lentamente."

    "El celular estaba vibrando constantemente."

        # SPRITE: MC perturbado

    "{color=[thought_color]}\"¿Asimilacion?\"{/color}"


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con % de asimilacion

    "{b}ASIMILACIÓN: 50%%{/b}"

    # SFX: vibración continua

    "La vibración continuó."

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2 - CONTINUAR DIALOGANDO CON LA VOZ
# ============================================================

label ruta_b2_dialogar:

    #sfx masa retorciendose 

    "Decides no moverse."

    "No tenias otra idea de qué otra cosa hacer."

    mc "¿Disculpe?"

    "La voz permaneció en silencio."

    "El sonido de algo retorciéndose continuaba alrededor."
    
    #infectado1 neutral

    infectado1 "Buenas noches."

    mc "¿Usted sabe dónde está la salida?"

    "Silencio."

    mc "¿Se encuentra bien?"

    "La voz comenzó a responder lentamente."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "{color=[thought_color]}\"Está repitiendo lo mismo.\"{/color}"
    "{color=[thought_color]}\"¿Esta menso?\"{/color}"

    infectado1 "¿Usted trabaja aquí?"

    mc "Sí."

    mc "En la tienda de helados."

    infectado1 "¿Uno de chocolate?"

    "Tragas saliva, algo no te gusta."

    mc "No."

    mc "Bueno..."

    mc "Hoy ya cerramos."

    "La voz permaneció en silencio."

    # SFX: golpe suave contra una pared

    "Entonces algo golpeó por todos lados"

    mc "¿Hola?"

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    infectado1 "Buenas noches."

    "Las palabras comenzaron a repetirse."

    "Cada vez más rápido."

    "Cada vez menos humanas."

    # EFFECT: distorsión

    "{color=[thought_color]}\"No quiero estar mas aqui\"{/color}"
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

    "Decides regresar sin pensarlo mucho y caminar."

    "La voz continuaba detrás de él."

    infectado1 "Buenas noches."

    infectado1 "¿Uno de chocolate?"

    infectado1 "Buenas noches."

    # SFX: masa retorciéndose aumentando
    #   BG de MC Huyendo de infectado 1 en medio de la plaza medio apagada, la cabeza debe estar por arriba con el cuello por todos lados

    "Caminar? Decides correr por tu vida "
    
    "Sientes que todo alrededor tuyo hay algo moviendose "

    "Al llegar a la tienda, cierras la puerta de golpe."

    "Permaneces completamnete perrturbado y agitado."

    # SFX: vibración

    "Entonces escuchó una vibración."

    "El celular que estaba en la tienda parece que recibio algo."

    "Aun con miedo, decides acercarte lentamente al teléfono."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 50%%{/b}"

    #Mc Viendo el celular 

    "El MC observó el teléfono."

    "La pantalla mostraba una notificación nueva."

    "{b}ASIMILACIÓN: 50%{/b}"

    "{color=[thought_color]}\"¿Qué significa esto?\"{/color}"
    "{color=[thought_color]}\"No, mas bien ¿Que mierda era esa persona?\"{/color}"

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2-B - CONTINUAR DIALOGANDO
# ============================================================

label ruta_b2_b:

    "Permaneces frente a la oscuridad con poca luz alrededor tuyo."

    "Intentas mantener la tranquilidad."

    mc "¿Usted trabaja aquí?"

    "..."

    infectado1 "Buenas noches."

    mc "¿Qué está haciendo en esta plaza, trabaja aqui?"

    "..."

    mc "¿Hola?"

    #BG infectado 1 rodeando al MC con el cuello por todos lados

    "El sonido alrededor comenzó a hacerse más fuerte de nudos y carne."

    "Como si algo enorme se estuviera moviendo por las paredes."

    infectado1 "Buenas noches."

    infectado1 "Es tarde para que se encuentre en este lugar."

    "{color=[thought_color]}\"Esto no tiene sentido.\"{/color}"
    "{color=[thought_color]}\"No fue buena idea hablar\"{/color}"

    "El MC miró hacia la oscuridad."

    mc "¿Quiere uno de chocolate?"

    "Silencio absoluto."


    infectado1 "Buenas noches."

    infectado1 "Uno de chocolate."

    # EFFECT: distorsión de voz

    infectado1 "Uno de chocolate."

    infectado1 "Uno de chocolate."

    infectado1 "UNO DE CHOCOLATE."

    infectado1 "UN0 D3 C'¿+´lA7E@"

    "{color=[thought_color]}\"No debí decir eso.\"{/color}"

    "Decides correr hacia la salida de la plaza sin importar nada."

    "Aunque claramente no veias la salida recuerdas aproximadamente donde ir, aunque tambien"

    "Hay algo moviendose por todos lados"

    "{color=[thought_color]}\"Mierda, Mierda\"{/color}"

    #bg tineda de helados 1 creo

    "Al llegar a la salida, cierras la puerta de golpe y sigues corriendo con todas tus fuerzas"

    "Pero una agradable vista de helados con un toque de vainilla indunda tu nariz"
    
    "Aunque en vez de tranquilizarte, te da un miedo extremo"

    #MC perturbado

    mc "'Que hago aqui."

    # SFX: vibración

    "Escuchas una vibración."

    "El celular que estaba en la tienda parece que recibio algo."

    "Aun con miedo, decides acercarte lentamente al teléfono."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 50%%{/b}"

    #Mc Viendo el celular 

    "La pantalla mostraba una notificación nueva."

    "{b}ASIMILACIÓN: 50%{/b}"

    "{color=[thought_color]}\"¿Qué significa esto?\"{/color}"
    "{color=[thought_color]}\"No, mas bien ¿Que mierda era esa persona?\"{/color}"


    # CORTE DE ESCENA

    return


# ============================================================
# RUTA B2-C - NO HACER NADA
# ============================================================

label ruta_b2_c:

    #BG infectado 1 rodeando al MC con el cuello por todos lados

    "Decides no responder."

    "No hacer ningún movimiento y quedarte como estatua."

    "..."

    "Tu capacidad de pensamiento lo notas lento."

    "Te sentias mareado."

    "Confundido."

    "Como si tu cuerpo ya no respondiera correctamente."

    "..."

    "La criatura continuaba observándolo."

    infectado1 "¿Se encuentra bien?"

    "Decides no responder."

    infectado1 "¿Necesita ayuda?"

    "..."

    #Screamer de infectado 1

    # EFFECT: distorsión progresiva
    # EFFECT: errores visuales
    # IMAGE: mensaje del ente el mero mero

    "\"¿Quién eres tú?\""

    "..."

    "\"Creo que puedo verte.\""

    "..."

    "\"Tal vez algún día logre entrar ahí también.\""

    # IMAGE: Infectado ocupando pantalla

    #TODO aqui tengo que ver como chingados hago el final 1 que sea un gameover dependiendo las acciones, no se como configurarlo aun pero ya que termine de poner esto bonito lo hare

    jump final_1_asimilacion


# ============================================================
# RUTA C - TIRAR EL CELULAR
# ============================================================

label tirar_celular:

    # SPRITE: MC tomando celular
    # BG: mostrador

    "Tomas el teléfono y sin pensarlo demasiado, lo arrojas dentro del bote de basura."

    "{color=[thought_color]}\"No es lo mismo dejarlo donde estaba que tirarlo a la basura.\"{/color}"
    "{color=[thought_color]}\"...¿Verdad?\"{/color}"

    "Te olvideas de eso y sales de la tienda."


    # ========================================================
    # LA SALIDA
    # ========================================================

    # BG: plaza después del apagón

    "sales rápidamente de la tienda."

    "Aunque cada paso se sentía más pesado que el anterior."

    "Te empiezas a fatigar y a sentirte mareado"
   
    #MC exhausto

    "{color=[thought_color]}\"¿Qué está pasando?\"{/color}"

    "El peso aumentó yan repentinamente que pierdes el equilibrio."

    "Caes de rodillas sobre el suelo."

    "Durante unos segundos no pudiste ni moverte."

    mc "¿Qué...?"

    "Intentas levantarse pero no puedes"

    # SFX: masa triturándose

    "Entonces escuchó un sonido de algo moviendose por todos lados."

    # ========================================================
    # EL INFECTADO 1 APARECE
    # ========================================================

    # SPRITE: INFECTADO 1
    # BG: plaza / criatura frente al MC viendo directo a la cara y en el piso
    # EFFECT: cuello extendiéndose

    "Una enorme cara se encontraba suspendida sobre de ti."

    "No tenía ojos normales"

    "Y parece que algo que solo con error puede describir la cara de la creatura."

    "Su cuello se extendía por todo el pasillo."

    "Giraba sobre sí mismo."

    "Se expandía, se contraia y se hacia una rueda misma con nudos por todos lados."

    "Desaparecía dentro de las paredes y aparecia por el techo."

    "Era imposible comprender pero un miedo tan extremo empezaba a romperte."

    "El horror recorrió tu cuerpo."

    infectado1 "Buenas tardes."

    infectado1 "¿Estará la gerente?"

    infectado1 "Quiero hablar sobre los horarios de apertura para la siguiente semana."

    "No podías procesar lo que te estaba diciendo."

    "Una cosa con cuello infinio te estaba hablando sobre horarios laborales?"

    "{color=[thought_color]}\"¿Qué mierda?\"{/color}"
    "{color=[thought_color]}\"¿Qué estoy viendo?\"{/color}"
    "{color=[thought_color]}\"¿Por qué está hablando como si fuera normall?\"{/color}"

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

    "Con las pocas fuerzas que te quedaban, corres hacia la puerta que tenía enfrente."

    "No miras hacia otro lado."

    "No te importaba el horror ni la fatiga que te hacia arrodillar."

    "No te importaba NADA."

    "Solo quería alejarte de lo que sea que estaba viendote."

    "Un cansancio tan extremo te estaba atormentando."

    "Detrás de ti, la voz de la creatura comenzó a elevarse."

    infectado1 "¡Buenos días!"

    infectado1 "¡Uno de chocolate, por favor!"

    #sfx puerta cerrandose

    "Llegas a la puerta la abrez y azotas detras de ti"


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    # BG: tienda de helados bg1
    # SPRITE: MC agitado y perturbado alv

    "Frente a ti se encontraba nuevamente el familiar puesto de helados."

    "El mostrador."

    "Las máquinas."

    "Los productos."

    "Todo parecía normal."

    "Demasiado normal?"

    "El aroma dulce característico del lugar no logró tranquilizarte en lo mas minimo."

    "Al contrario."

    "te recordó lo poco logico que es estar aqui."

    "El miedo inunda tu cuerpo una vez mas."

    "Tu respiración se volvió aun mas irregular."

    "La hiperventilación te impedía pensar correctamente."

    "Pasaron varios minutos."

    "Permaneces dentro del local intentando recuperar la calma."

    "{color=[thought_color]}\"Respira.\"{/color}"
    "{color=[thought_color]}\"Solo respira.\"{/color}"
    "{color=[thought_color]}\"No necesitas entender ahora mismo que esta pasando\"{/color}"
    "{color=[thought_color]}\"Solo, necesitas volver a ti.\"{/color}"

    # SFX: vibración 
    #Me gustaria hacer un tipo screamer del MC con el celular, que a todos nos a espantado una mmda
    #BG personalizado del MC horrorizado y usado para hacer un screamer basico tirado en el puesto de helados y el bote se basura con luz del celular

    "Casi te cagas del susto que te da un sonido."

    "Una vibración."

    "El celular que estaba dentro del bote de basura."

    "Decides ver dentro del bote de basura y ver porque esta vibrando."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 80%%{/b}"

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA C2 - DIALOGAR CON EL INFECTADO
# ============================================================

label ruta_c2_dialogar:

    "Te armas de valor y decides hablar con lo que tienes enfrente"

    "Nunca habías sentido un miedo semejante de estar aquí."

    "Las palabras apenas lograban tener coherencia"

    mc "B-buenas noches."

    mc "L-la gerente se ha ido más temprano."

    "El ambiente comenzó a romperse."

    "No físicamente."

    "O quizás sí."

    "Era imposible saberlo."

    "El sonido alrededor parecía distorsionarse."

    "Un horror aun mas fuerte te invadio cada fibra de tu ser"

    "La voz del Infectado respondió."

    infectado1 "Buenas noches."

    infectado1 "Es una pena."

    infectado1 "Favor de decir que la siguiente semana se..."

 
    # EFFECT: distorsión fuerte de voz se tiene que dar entender que lo que tiene que ver con la siguiente semana 
    #ES UN MISTERO y no se puede decir, mencionar ni sugerir
    #Es como silenciar al infectado


    "La voz se distorsionó completamente las palabras perdieron su sonido y tus sentidos dejaron de estar conectados a ti."

    "Despues vuelves a escuchar."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    "Permaneces completamente inmóvil y sin lograr pensar."

    "Desde tu visión periférica comeienzas a divisar algo"

    "Un cuello?"

    "Recorriendo todo el centro de la plaza."

    "Atravesando paredes."

    "Desapareciendo dentro de estructuras."

    "Extendiéndose mucho más allá de lo que podía comprender y haciendo nudos por todos lados."

    "La cabeza del Infectado te observaba mas fijamente."

    "{color=[thought_color]}\"¿Que chingados es todo esto? NO QUIERO MORIR\"{/color}"

    "La criatura inclinó ligeramente la cabeza."

    infectado1 "¿Se encuentra bien?"

    infectado1 "¿Necesita ayuda?"

    "El miedo nubla tu juicio"

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

    "Con todo y panico que esta en cada parte de tu cuerpo, decides responder con la verdad."

    mc "E-estaba buscando la salida."

    mc "S-solo que me tropecé un poco."

    "Tragas saliva instintivamente."

    "Ni siquiera tu mente podia procesar lo que tu vista alcanza a ver"

    "Un miedo aun peor de intentar razonar lo que pasa te nubla mas"

    "El Infectado permanece observándote."

    "Durante unos segundos mas no dijo nada."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    "Si existiera algo que te pudiera poner peor, era eso."

    infectado1 "Buenas noches."

    infectado1 "Quiero uno de chocolate sencillo, por favor."

    "El pánico aumentó tanto que tu cuerpo termina colapsando."

    "Las palabras que escuchas se distorsionan y escuchan dentro de tus oidos."


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
    # Tiene que transmitir un sentimiento de que fuiste abrumado por algo, para que puedan entender esto imagenen lo siguiente
    #En tu campo visual y todo lo que logras ver imagina una cara que abarca todo lo que ves, al razonar eso escuchas la misma cosa repitiendose
    #Si intentas tomar en serio ese ejemplo, te da un miedo existencial y eso busco transmitir aqui

    #BG corriendo del infectado 1 con el cuello por todos lados y la cabeza por arriba de la pantalla

    "La voz te terminaria dejando loco."

    "No aguantaste mas esta situacion"

    "{color=[thought_color]}\"  NO PUEDO SEGUIR AQUI.\"{/color}"

    "Decides correr hacia la salida."

    "Llegas a la puerta la abrez y azotas detras de ti"


    # ========================================================
    # REGRESO A LA TIENDA
    # ========================================================

    # BG: tienda de helados bg1
    # SPRITE: MC agitado y perturbado alv

    "Frente a ti se encontraba nuevamente el familiar puesto de helados."

    "El mostrador."

    "Las máquinas."

    "Los productos."

    "Todo parecía normal."

    "Demasiado normal?"

    "Aunque con tanto miedo ni siquiera logras analizar que estas en la tienda de helados y no en la salida de la plaza."

    "Tu respiración se volvió aun mas irregular."

    "La hiperventilación te impedía pensar correctamente."

    "Pasaron varios minutos."

    "Permaneces dentro del local intentando recuperar la calma."

    "{color=[thought_color]}\"Respira.\"{/color}"
    "{color=[thought_color]}\"Solo respira.\"{/color}"
    "{color=[thought_color]}\"No entiendo que era, no entiendo que hago aqui, no entiendo porque intento entender.\"{/color}"
    "{color=[thought_color]}\"Solo, necesitas volver a ti.\"{/color}"

    # SFX: vibración 
    #Me gustaria hacer un tipo screamer del MC con el celular, que a todos nos a espantado una mmda
    #BG personalizado del MC horrorizado y usado para hacer un screamer basico tirado en el puesto de helados y el bote se basura con luz del celular

    "Casi te cagas del susto que te da un sonido."

    "Una vibración."

    "El celular que estaba dentro del bote de basura."

    "Decides ver dentro del bote de basura y ver porque esta vibrando."


    # ========================================================
    # NOTIFICACIÓN
    # ========================================================

    # IMAGE: celular con notificación

    "{b}ASIMILACIÓN: 80%%{/b}"

    # CORTE DE ESCENA

    return


# ============================================================
# RUTA C2-B - NO HACER NADA
# ============================================================

label ruta_c2_b:

    # BG: plaza oscura
    # SPRITE: Infectado 1

    "No respondes."

    "No haces ningún movimiento."

    "Permaneces completamente inmóvil."

    "..."

    "Tu capacidad de pensamiento comienza a fallar."

    "La criatura continuaba observándote."

    infectado1 "¿Te encuentras bien?"

    "..."

    #Screamer de infectado 1

    # EFFECT: distorsión progresiva
    # EFFECT: errores visuales
    # IMAGE: mensaje del ente el mero mero

    "\"¿Quién eres tú?\""

    "..."

    "\"Creo que puedo verte.\""

    "..."

    "\"Tal vez algún día logre entrar ahí también.\""

    # IMAGE: Infectado ocupando pantalla

    #TODO aqui tengo que ver como chingados hago el final 1 que sea un gameover dependiendo las acciones, no se como configurarlo aun pero ya que termine de poner esto bonito lo hare

    jump final_1_asimilacion

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

    "Parece mirar al jugador."

    

    # EFFECT: zoom lento
    # EFFECT: distorsión progresiva
    # SFX: voces repetidas
    

    #AQUI ESTA ESTO DEL FINAL NO SE COMO HACERLO PERO YA ME DARE UN TIRO JUNTO AL PROGRAMADOR DE DARLE SENTIDO A ESTO

    #### voy a ver si puedo ordenar los finales en un mismo archivo para evitar hacer 1000 lineas de codigo


    # ========================================================
    # MECÁNICA ESPECIAL DEL FINAL
    # ========================================================

    # TODO:
    # Al cerrar y volver a abrir el juego, no se debe llegar al menu si no a la misma imagen y que salga un boton que diga reinicio despues de unos segundos
    # Al reiniciarlo debe estar el juego como si anda y todo nuevo
    # TODO:

    # Hasta que no se ponga ese boton, la escena deberá permanecer activa.

    while True:
        pause

##### no pongas mas lineas de codigo de aqui, hay que hacer nuevos archivos para continuar las cosas y ahora mismo todo esto es el capitulo 1 de la demo 1