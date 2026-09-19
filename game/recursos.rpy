##### Personajes de la demo 1 #####

define mc = Character("Pedro")
define infectado1 = Character("Infectado")

# Color de los pensamientos del MC. Uso:  "{color=[thought_color]}\"Texto del pensamiento.\"{/color}"
define thought_color = "#8ecae6"

# TODO: darle color a los nombres cuando se defina el estilo final de la caja de dialogo, ejemplo Character("Pedro", who_color="#8ecae6")
# TODO: definir aqui a los demas infectados / personajes (la gerente, el ente "el mero mero") cuando aparezcan en pantalla


#### Imagenes definidas del menu #####
image main_menuvid = Movie(play="images/bg/main_menuvid.webm", loop=True)


#### Imagenes definidas backgroung "bg" ####

image bg1 = "images/bg/bg1.png"                 # Puesto de helados visto desde adentro (mira hacia la plaza)
image bg2 = "images/bg/bg2.jpg"                 # Mostrador del puesto de helados
image bgcelular = "images/bg/bgcelular.jpg"     # Mostrador con el celular (Nokia) encima

# TODO: faltan los BG de la plaza (pasillo, salida, plaza oscura, plaza con luces parpadeando) y los BG del infectado 1


#### Imagenes definidas de personajes ####
#### Todas las expresiones del MC comparten la etiqueta "mc", asi que al mostrar una nueva
#### reemplaza a la anterior y no se apilan. Uso en el script:  show mc pensante
#### Nota: el "Nivel" es lo que baja de sanidad segun la tabla del script (funcion miedo() en sistemas_demo.rpy)

## Sin miedo
image mc neutral = "images/sprites/mc_neutral.png"
image mc feliz = "images/sprites/mc_feliz.png"
image mc pensante = "images/sprites/mc_pensante.png"
image mc analizando = "images/sprites/mc_analizando.png"
image mc alerta = "images/sprites/mc_alerta.png"
image mc hablando1 = "images/sprites/mc_hablando1.png"      # De espaldas, volteando a ver mientras habla
image mc hablando2 = "images/sprites/mc_hablando2.png"      # De perfil, hablando con la palma abierta

## Con miedo (de menor a mayor)
image mc incomodo = "images/sprites/mc_incomodo.png"                # Nivel 1: -2
image mc nervioso = "images/sprites/mc_nervioso.png"                # Nivel 2: -5
image mc nervioso_2 = "images/sprites/mc_nervioso_2.png"            # Nivel 2: -5 (variante)
image mc asustado = "images/sprites/mc_asustado.png"                # Nivel 3: -10
image mc aterrado = "images/sprites/mc_aterrado.png"                # Entre nivel 3 y 4 (no esta en la tabla, vea TODO en sistemas_demo.rpy)
image mc aterrado_2 = "images/sprites/mc_aterrado_2.png"            # Entre nivel 3 y 4 (variante)
image mc aterrorizado = "images/sprites/mc_aterrorizado.png"        # Nivel 4: -20
image mc colapso = "images/sprites/mc_colapso.png"                  # Nivel 5: -30
image mc colapso_2 = "images/sprites/mc_colapso_2.png"              # Nivel 5: -30 (con glitch, ideal para el final / distorsion)

# TODO: faltan los sprites del infectado 1 (base sin glitch, cabeza alargada, cuello por todos lados, cara ocupando pantalla)
