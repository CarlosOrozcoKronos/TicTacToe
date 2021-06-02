import constantes as CONSTANTES


class Tablero:
    """
    muestra el tablero, que contiene las fichas, puede devolver la posicion de
    las mismas
    123
    456
    789
    """

    def __init__(self):
        self.tablero = [[CONSTANTES.BLANCK, CONSTANTES.BLANCK, CONSTANTES.BLANCK],
                        [CONSTANTES.BLANCK, CONSTANTES.BLANCK, CONSTANTES.BLANCK],
                        [CONSTANTES.BLANCK, CONSTANTES.BLANCK, CONSTANTES.BLANCK]]

    def getXYDePosicion(self, posicion):
        posx = (posicion % 3) - 1
        if posx == -1:
            posx = 2
        posy = 0
        if posicion >= 7:
            posy = 2
        elif posicion >= 4:
            posy = 1
        return (posy, posx)

    def getPosicionDeXY(self, posX, posY):
        """
        donde X es la casilla e Y es la linea
        """
        posicion = (posX + 1) + posY * 3
        return posicion

    def insertarFicha(self, ficha, posicion):
        """
        ficha = X o O
        posicion numero de 1 a 9
        """
        YX = self.getXYDePosicion(int(posicion))
        self.tablero[YX[0]][YX[1]] = self.traducirFicha(ficha)

    def traducirFicha(self, ficha):
        """
        devuelve el valor numerico de la ficha o su simbolo
        """
        if ficha in CONSTANTES.FICHAS:
            return (CONSTANTES.FICHAS.index(ficha) - 1)
        elif (ficha + 1) in range(len(CONSTANTES.FICHAS)):
            return CONSTANTES.FICHAS[ficha + 1]
        raise Exception("Ficha no valida")

    def mostrarTablero(self):
        print()
        for linea in self.tablero:
            print(f"{self.traducirFicha(linea[0])}|{self.traducirFicha(linea[1])}|{self.traducirFicha(linea[2])}")

    def getCasillasVacias(self):
        """
        tambien se puede contar hasta turno 9, esto valdria para tableros
        de mas de 3X3
        """
        y = 0
        vacias = []
        for linea in self.tablero:
            x = 0
            for casilla in linea:
                if casilla is CONSTANTES.BLANCK:
                    vacias.append(self.getPosicionDeXY(x, y))
                x += 1
            y += 1
        return(vacias)
