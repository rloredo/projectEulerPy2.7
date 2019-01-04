class grid(object):
    def __init__(self, col_amount, row_amount):

        self.grid = [] # lista vacia que recibe todas las row
        rowTemp = [] # crea filas que luego se agregan como listas
        self.posicion = [0,0]

        for row in range(row_amount):
            for col in range(col_amount):
                rowTemp.append(0)
            self.grid.append(rowTemp)
            rowTemp = []

    def cambiarValorCelda(self, x):
        self.grid[self.posicion[0]][self.posicion[1]] = x

    def actualizarPosicion(self,x,y):
        self.posicion = [x,y]  #x = fila / y = columna

    def valorPosicionActual(self):
        return self.grid[self.posicion[0]][self.posicion[1]]

    def moverIzq(self):
        if self.posicion[1] == 0:
            print 'fuera de rango'
            return False
        else:
            self.posicion[1] = self.posicion[1] - 1
            return True

    def moverDerecha(self):
        if self.posicion[1] == len(self.grid[0]):
            print 'fuera de rango'
            return False
        else:
            self.posicion[1] = self.posicion[1] + 1
            return True

    def moverArriba(self):
        if self.posicion[0] == 0:
            print 'fuera de rango'
            return False
        else:
            self.posicion[0] = self.posicion[0] - 1
            return True

    def moverAbajo(self):
        if self.posicion[0] == len(self.grid):
            print 'fuera de rango'
            return False
        else:
            self.posicion[0] = self.posicion[0] + 1
            return True

    def obtenerFila(self, x):
        return self.grid[x]

    def obtenerColumna(self, x):
        col = []
        for row in range(len(self.grid)):
            col.append(self.grid[row][x])
        return col

    def obtenerDiagonalDerAbj(self, x, y): #x, y indica punto de inicio de la diagonal
            guardarValorInicial = self.posicion
            self.actualizarPosicion(x,y)
            diagonal = []
            while self.posicion[1] != len(self.grid) and self.posicion[0] != len(self.grid[1]):
                    diagonal.append(self.valorPosicionActual())
                    self.moverAbajo()
                    self.moverDerecha()
            self.actualizarPosicion(guardarValorInicial[0], guardarValorInicial[1])
            return diagonal

    def obetenerDiagonalIzqAbj(self, x, y): #Funciona para iterar por columna, pero por fila tiene problemas
            guardarValorInicial = self.posicion
            self.actualizarPosicion(x,y)
            diagonal = []
            while self.posicion[1] != 0 and self.posicion[0] != len(self.grid):
                    diagonal.append(self.valorPosicionActual())
                    self.moverIzq()
                    self.moverAbajo()
            if self.posicion[1] == 0:
                diagonal.append(self.valorPosicionActual())
            self.actualizarPosicion(guardarValorInicial[0], guardarValorInicial[1])
            return diagonal


    def obetenerDiagonalIzqAbj2(self, x, y): #Resuelve problema con la break condition cuando itera sobre filas en misma columna
            guardarValorInicial = self.posicion
            self.actualizarPosicion(x,y)
            diagonal = []
            while self.posicion[1] != -1 and self.posicion[0] != len(self.grid):
                    diagonal.append(self.valorPosicionActual())
                    self.moverIzq()
                    self.moverAbajo()
            self.actualizarPosicion(guardarValorInicial[0], guardarValorInicial[1])
            return diagonal


    def cambiarCol(self, x, l): #x col / l lista reemplazo empieza en row 0

        if len(l) > self.grid[x]:
            print 'fuera de rango'

        else:
            guardarValorInicial = self.posicion
            self.actualizarPosicion(0,x)
            for elem in range(len(l)):
                self.cambiarValorCelda(l[elem])
                self.moverAbajo()
            self.actualizarPosicion(guardarValorInicial[0], guardarValorInicial[1])

    def cambiarFil(self, x, l): #x fila / l lista reemplazo empieza en col 0

        if len(l) > self.grid[x]:
            print 'fuera de rango'

        else:
            guardarValorInicial = self.posicion
            self.actualizarPosicion(x,0)
            for elem in range(len(l)):
                self.cambiarValorCelda(l[elem])
                self.moverDerecha()
            self.actualizarPosicion(guardarValorInicial[0], guardarValorInicial[1])

    def cargarDeLista(self, l):
            guardarValorInicial = self.posicion
            self.actualizarPosicion(0,0)
            if len(l) != len(self.obtenerColumna(0)) * len(self.obtenerFila(0)):
                print 'fuera de rango'
            else:
                inicio = 0
                for columnas in range(len(self.obtenerColumna(0))):
                    for espacio in range(len(self.obtenerFila(0))):
                        self.cambiarValorCelda(l[inicio + espacio])
                        self.moverDerecha()
                    self.actualizarPosicion(self.posicion[0],0)
                    self.moverAbajo()
                    inicio = inicio + len(self.obtenerFila(0))
