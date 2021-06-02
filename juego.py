import tablero as tabletop
import jugador as Gamer
import constantes as CONSTANTES


class Juego:

    def __init__(self):
        self.turno = 0
        self.tablero = tabletop.Tablero()
        self.jugador1 = Gamer.Jugador(CONSTANTES.FICHAS[2])
        self.jugador2 = Gamer.Jugador(CONSTANTES.FICHAS[0])

    def jugadaEsValida(self, jugada, vacias):
        return str(jugada).isdigit() and int(jugada) in vacias

    def pedirJugada(self, jugadorXO):
        return jugadorXO.jugada(self.turno, self, self.tablero)

    def turnoLooper(self):
        while (not self.gameOver()):
            self.turno += 1
            if self.turno % 2:
                self.tablero.insertarFicha(self.jugador1.ficha, self.pedirJugada(self.jugador1))
            else:
                self.tablero.insertarFicha(self.jugador2.ficha, self.pedirJugada(self.jugador2))
            self.tablero.mostrarTablero()

    def ganado(self):
        return False

    def gameOver(self):
        if self.turno >= 9 or self.ganado():
            print("GAME OVER")
            return True
        return False
