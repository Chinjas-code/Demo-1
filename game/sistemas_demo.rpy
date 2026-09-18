#### IA DE INFECTADOS ####
#### Aqui es el apartado de como funcionara el sistema de IA del juego para determinar si un INFECTADO nos atacara o nos dejara libre terminando un final u otro del juego. ####


default normalidad = 100 # Normalidad: Qué tan bien el MC mantiene su "papel". Ejemplo el MC tiene que dar respuestas que van acorde a lo "normal" o a su "rol". Vea linea "" de script.rpy
default asimilacion = 0 # Asimilación: Qué tan Asimilado está con la anomalía. Ejemplo MC llega 100% = Final 1, ademas ayuda a dar el nivel de amenaza.
default sanidad = 100 # Sanidad: Qué tan afectado mentalmente está, solo disminuye en esta demo. Importante despues tendra la funcion de recuperarse de una uh otra manera, ahora mismo ayuda a determinar el nivel de Amenaza + depende la expresion que tenga el mc en la tabla que puse en script. (mas abajo esta su propio apartado)
      

init python:

    import random

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
        dado = random.randint(1, 100)

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

        valores = {
            "incomodo": 2,
            "nervioso": 5,
            "asustado": 10,
            "aterrorizado": 20,
            "colapso": 30
        }

        sanidad -= valores.get(expresion, 0)

        sanidad = max(0, sanidad)

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


