import juego
import tablero
import os


class Jugador:

    def __init__(self, miFicha):
        self.ficha = miFicha

    def jugada(self, turno, juego, tablero):
        """
        juego es un objero de tipo juego, tablero es de tipo tablero
        """
        print(f"Es el turno de jugador :{turno},")
        print("introduce en que casilla quieres tu ficha")
        vacias = tablero.getCasillasVacias()
        print(f"solo quedan las casillas {vacias}")
        miJugada = input("123\r\n456\r\n789\r\n")
        while (not juego.jugadaEsValida(miJugada, vacias)):
            print("has introducido una jugada no valida,")
            print(f"recuerda que solo quedan las casillas {vacias}")
            miJugada = input("123\r\n456\r\n789\r\n")
        os.system("cls" if os.name == "nt" else "clear")
        return miJugada
