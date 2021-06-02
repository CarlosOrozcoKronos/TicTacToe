import juego
import tablero


class Jugador:

    def __init__(self):
        pass

    def jugada(self, turno, juego, tablero):
        """
        juego es un objero de tipo juego, tablero es de tipo tablero
        """
        print(f"Es el turno de jugador :{turno},")
        print("introduce en que casilla quieres tu ficha")
        vacias = tablero.getCasillasVacias()
        print(f"solo quedan las casillas {vacias}")
        miJugada = input("123\r\n456\r\n789")
        while (not juego.jugadaEsValida(miJugada, vacias)):
            print("has introducido una jugada no valida, introduce:")
            print(f"recuerda que solo quedan las casillas {vacias}")
            miJugada = input("123\r\n456\r\n789")
        return miJugada
