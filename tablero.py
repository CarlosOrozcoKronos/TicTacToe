# CONTANTES
x = 1
O = -1
BLANCK = 0

class Tablero:
    """
    muestra el tablero, que contiene las fichas, puede devolver la posicion de las mismas
    """


    def __init__(self):
        self.tablero = [[[BLANCK],[BLANCK],[BLANCK]],
                [[BLANCK],[BLANCK],[BLANCK]],
                [[BLANCK],[BLANCK],[BLANCK]]]
    
    def insertarFicha(self, ficha, posicion):
        """
        ficha = X o O
        posicion numero de 1 a 9
        """
        pass


    def mostrarTablero(self):
        pass


    def setFicha(self):
        pass


    def getTablero(self):
        return self.tablero
