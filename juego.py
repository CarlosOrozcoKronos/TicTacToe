class Juego:

    def __init__(self):
        self.turno = 0

    def jugadaEsValida(self, jugada, vacias):
        return str(jugada).isdigit() and int(jugada) in vacias

    def pedirJugada(self):
        pass

    def turno(self):
        pass

    def gameOver(self):
        pass
