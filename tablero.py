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
        linterTester = "cadena corta" + "cadena larga asidaidjasdjaksdjaklsdjaskldjaskdjaskdjjaksdaksdñjlkasdjkalñsjdaksdjkaljsdkñasjdasdklñajsdklajs"
        print(linterTester)
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

    def linea(self, ficha):
        for linea in self.tablero:
            suma = 0
            for casilla in linea:
                suma += casilla
            if suma == (self.traducirFicha(ficha) * 3):
                return True
        return False

    def columna(self, ficha):
        suma = []
        for linea in self.tablero:
            suma.append(0)
        for linea in self.tablero:
            i = 0
            for casilla in linea:
                suma[i] += casilla
                i += 1
        if (self.traducirFicha(ficha) * 3) in suma:
            return True
        return False

    def diagonal(self, ficha):
        sumaDiagPositiva = 0
        sumaDiagNegativa = 0
        j = 0
        for linea in self.tablero:
            i = 0
            for casilla in linea:
                # Calcular primera, media y ultima
                if i == j:
                    sumaDiagPositiva += casilla
                if j == ((len(linea) - 1) - i):
                    sumaDiagNegativa += casilla
                i += 1
            j += 1
        if sumaDiagPositiva == (self.traducirFicha(ficha) * 3) or sumaDiagNegativa == (self.traducirFicha(ficha) * 3):
            return True
        return False
