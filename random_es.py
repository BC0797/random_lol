import random

def nombre_jugadores(cantidad_jugadores):
    jugadores = []
    contador = 0
    while contador < cantidad_jugadores:
        jugadores.append(input(f'Jugador {contador + 1}: '))
        contador += 1
    return (jugadores)


def numero_equipo(jugadores):
    orden_equipo = []
    contador = 0
    while contador < jugadores:
        numero = random.choice(range(0,10,1))
        if numero in orden_equipo:
            if len(orden_equipo) == jugadores:
                break
            else:
                continue
        else:   
            orden_equipo.append(numero)
    contador += 1
    return(orden_equipo)
    
def posiciones(jugadores, orden):
    match = []
    contador = 0
    while contador < len(jugadores):
    # for jugador in jugadores-1:
        posicion = input('Posicion: ')
        jugador_1 = jugadores[orden[contador]]
        jugador_2 = jugadores[orden[contador +1]]
        match.append(f'{posicion}: {jugador_1} vs {jugador_2}')
        print(f'{posicion}: {jugador_1} vs {jugador_2}')
        contador += 2
    print("")
    for element in match:
        print(element)
    return match

def run():
    cantidad_jugadores = 10 #int(input('Cantidad de jugadores: '))
    nombres = nombre_jugadores(cantidad_jugadores)
    orden = numero_equipo(cantidad_jugadores)
    jugadores_posicion_equipo = numero_equipo(cantidad_jugadores)
    posiciones(nombres, orden)
    

if __name__ == '__main__':
    run()
