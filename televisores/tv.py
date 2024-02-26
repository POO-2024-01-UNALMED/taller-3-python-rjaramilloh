class TV:
    _numTv = 0
    def __init__(self,marca,estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV._numTv+=1

    @classmethod
    def getNumTv(cls):
        return cls._numTv

    @classmethod
    def setNumTv(cls , numTv):
        cls._numTv = numTv

    def turnOn (self):
        self._estado = True

    def turnOff (self):
        self._estado = False

    def getEstado (self):
        return self._estado
#////////////////////////////////////////////
    def canalUp (self):
        if (self._canal < 120 and self._estado == True):
            self._canal+=1

    def canalDown (self):
        if (self._canal > 1 and self._estado == True):
            self._canal-=1

    def volumenUp (self):
        if (self.volumen < 7 and self.estado == True):
            self.volumen+=1

    def volumenDown (self):
        if (self.volumen > 0 and self.estado == True):
            self.volumen-=1
#/////////////////////////////////////////////
    def setMarca (self, marca):
        self._marca = marca

    def getMarca (self):
        return self._marca

    def setCanal (self, canal):
        self._canal = canal

    def getCanal (self):
        return self._canal

    def setPrecio (self, precio):
        self._precio = precio

    def getPrecio (self):
        return self._precio

    def setVolumen (self, volumen):
        if (0<=volumen and volumen<=7 and self._estado == True):
            self._volumen = volumen

    def getVolumen (self):
        return self._volumen

    def setControl (self, control):
        self._control = control

    def getControl (self):
        return self._control
