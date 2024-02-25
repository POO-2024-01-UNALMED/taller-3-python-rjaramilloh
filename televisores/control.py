class Control:

    def __init__(self,tv):
        self._tv=tv
    
    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalUp()
    
    def volumeUp(self):
        self._tv.volumenUp()
    
    def setCanal(self, canal):
        self._tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)
    
    def enlazar (self, tv):
        tv.setControl(self)
        self._tv = tv
    
    def getTv (self):
        return self._tv
    
    def setTv (self , tv):
        self._tv=tv
