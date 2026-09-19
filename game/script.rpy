
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


#### ACTUALIZACION (expresiones del MC y narracion)
#### Toda la narracion esta en PRIMERA PERSONA (yo). Los dialogos de mc / infectado1 no se tocaron.
#### Las expresiones del MC se muestran con:  show mc <expresion>   (definidas en recursos.rpy)
####   neutral, feliz, pensante, analizando, alerta, hablando1, hablando2,
####   incomodo, nervioso, nervioso_2, asustado, aterrado, aterrado_2, aterrorizado, colapso, colapso_2
#### Donde dice "# TODO miedo(...)" es donde se debe restar sanidad (ver sistemas_demo.rpy), todavia NO se llama.
#### Donde dice "# TODO" es algo que falta por hacer (BG, sprites, efectos, sonidos, etc).


#### COMO FUNCIONA ESTA LOGICA DE ESTA DEMO #####

# Expresión del MC = En este caso, dependiendo que PNG pongamos sera que se le reste un valor determinado de su "Sanidad".
# Incómodo 1 −2 Algo extraño, pero tolerable.
# Nervioso 2 −5 Percibe que algo no está bien.
# Asustado 3 −10 Ve o escucha algo claramente anormal.
# Aterrorizado 4 −20 Un infectado o evento amenaza su percepción.
# Colapso 5 −30 Evento extremo o traumático.

#### Lean PDF apartado de "sistemas (Apartado de IA infectados)" ahi especifico como funcionara la IA que determinara el % de amenaza del infectado que nos vaya atacar dependiendo
#### las acciones que el jugador haga sobre esta demo.


#### MAPA DE ARCHIVOS (script.rpy ya NO tiene la historia, solo arranca el juego) ####
####
####   game/
####   |- script.rpy ......................... label start (entrada del juego), notas generales
####   |- recursos.rpy ....................... personajes, fondos y sprites definidos
####   |- sistemas_demo.rpy .................. variables y funciones de sanidad / amenaza / IA / asimilacion
####   |- sistemas/
####   |   |- inventario.rpy ................. objetos, add_item / has_item / use_item y pantalla del inventario (tecla I)
####   |   |- telefono_nokia.rpy ............. bateria, pantalla del Nokia y glitch segun la asimilacion
####   |- capitulos/
####   |   |- capitulo_1/
####   |   |   |- cap1_inicio.rpy ............ inicio + menu del celular (label capitulo_1)
####   |   |   |- cap1_ruta_a_tomar.rpy ...... RUTA A: tomar el celular
####   |   |   |- cap1_ruta_b_dejar.rpy ...... RUTA B: dejar el celular (b1, b2, b2_a, b2_b, b2_c)
####   |   |   |- cap1_ruta_c_tirar.rpy ...... RUTA C: tirar el celular (c1, c2, c2_a, c2_b)
####   |   |- capitulo_2/
####   |       |- cap2_inicio.rpy ............ AQUI SE ESCRIBE EL CAPITULO 2 (label capitulo_2), trae una escena de prueba del Nokia
####   |- finales/
####       |- finales.rpy .................... todos los finales del juego, ordenados
####
#### Flujo:  start -> capitulo_1 -> (ruta A / B / C) -> capitulo_2   o   -> un final (finales.rpy)
#### Para el capitulo 3 crear la carpeta capitulos/capitulo_3/ con cap3_inicio.rpy (label capitulo_3) y
#### al final del capitulo 2 poner "jump capitulo_3".


label start:

    jump capitulo_1
