#### IA DE INFECTADOS ####
#### Aqui es el apartado de como funcionara el sistema de IA del juego para determinar si un INFECTADO nos atacara o nos dejara libre terminando un final u otro del juego. ####


default normalidad = 100 # Normalidad: Qué tan bien el MC mantiene su "papel". Ejemplo el MC tiene que dar respuestas que van acorde a lo "normal" o a su "rol". Vea linea "" de script.rpy
default asimilacion = 0 # Asimilación: Qué tan Asimilado está con la anomalía. Ejemplo MC llega 100% = Final 1, ademas ayuda a dar el nivel de amenaza.
default sanidad = 100 # Sanidad: Qué tan afectado mentalmente está, solo disminuye en esta demo. Importante despues tendra la funcion de recuperarse de una uh otra manera, ahora mismo ayuda a determinar el nivel de Amenaza + depende la expresion que tenga el mc en la tabla que puse en script. (mas abajo esta su propio apartado)
      

# "asimilacion" ya se usa en 3 lugares: la notificacion del celular en cada ruta del capitulo 1 (le pone el valor:
# 10%, 50% u 80%), la funcion calcular_amenaza() de aqui abajo y el Nokia (sistemas/telefono_nokia.rpy), que se
# va corrompiendo (glitch) mientras mas alta este.
# TODO: "normalidad" no baja en ninguna parte, hay que decidir que respuestas del jugador la bajan (ver PDF).

init python:

    # Sube o baja la asimilacion (0 a 100). Ej: $ change_terror(20)  /  $ change_terror(-5)
    # (el nombre viene del sistema de inventario del companero, se dejo igual para no romper sus ejemplos)
    def change_terror(amount):

        global asimilacion

        asimilacion = max(0, min(100, asimilacion + amount))

        renpy.restart_interaction()


    def calcular_amenaza():

        vulnerabilidad = 100 - sanidad
        perdida_normalidad = 100 - normalidad

        amenaza = (
            (asimilacion * 0.40) +
            (vulnerabilidad * 0.30) +
            (perdida_normalidad * 0.30)
        )

        amenaza = max(0, min(100, amenaza))

        return amenaza


    def infectado_decide_atacar():

        probabilidad = calcular_amenaza()

        # renpy.random en vez de random para que el resultado sea igual al volver atras (rollback) o cargar partida
        dado = renpy.random.randint(1, 100)

        if dado <= probabilidad:
            return True
        else:
            return False


#### SISTEMA DE MIEDO ####


#### SISTEMA DE MIEDO PARA USAR DENTRO DE LA DEMO ####
#### Lean el PDF pero basicamente cada que algo suceda, se le baja determinando que tanto miedo tuvo el prota, servira despues para el % final de AMENAZA

init python:

    def miedo(expresion):

        global sanidad

        # TODO: las expresiones "aterrado" y "aterrado_2" (recursos.rpy) no estan en esta tabla, hay que decidir cuanto restan
        # (algo entre asustado -10 y aterrorizado -20) y agregarlas aqui.
        valores = {
            "incomodo": 2,
            "nervioso": 5,
            "asustado": 10,
            "aterrorizado": 20,
            "colapso": 30
        }

        sanidad -= valores.get(expresion, 0)

        sanidad = max(0, sanidad)

# TODO: miedo() todavia no se llama en script.rpy. Los lugares donde se debe llamar estan marcados con "# TODO miedo(...)" al lado de cada expresion.
#### EJEMPLO DE USO DE CODIGO: ####

# Normalidad = 60
# Asimilación = 20
# Sanidad = 50
# Vulnerabilidad = 100 - 50 = 50
# Pérdida de Normalidad = 100 - 60 = 40
# 20 × 0.40 = 8
# 50 × 0.30 = 15
# 40 × 0.30 = 12
# Amenaza = 8 + 15 + 12 = 35
# TODO Probabilidad de ataque = 35%


