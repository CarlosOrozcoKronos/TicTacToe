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
        ficha = None
        while (not self.gameOver(ficha)):
            self.turno += 1
            if self.turno % 2:
                ficha = self.jugador1.ficha
                self.tablero.insertarFicha(ficha, self.pedirJugada(self.jugador1))
            else:
                ficha = self.jugador2.ficha
                self.tablero.insertarFicha(ficha, self.pedirJugada(self.jugador2))
            self.tablero.mostrarTablero()

    def ganado(self, ficha):
        if self.tablero.linea(ficha) or self.tablero.columna(ficha) or self.tablero.diagonal(ficha):
            return True
        return False

    def gameOver(self, ficha):
        if ficha is None :
            return False
        if self.turno >= 9 or self.ganado(ficha):
            print("GAME OVER")
            return True
        return False
