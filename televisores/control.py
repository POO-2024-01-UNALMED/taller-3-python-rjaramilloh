class Control:

    def __init__(self):
        self._tv=None
    
    def turnOn(self):
        if self.tv:
            self._tv.turnOn()

    def turnOff(self):
        if self.tv:
            self._tv.turnOff()

    def canalUp(self):
        if self.tv:
            self._tv.canalUp()
    
    def canalDown(self):
        if self.tv:
            self._tv.canalUp()
    
    def volumeUp(self):
        if self.tv:
            self._tv.volumenUp()
    
    def setCanal(self, canal):
        if self.tv:
            self._tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        if self.tv:
            self._tv.setVolumen(volumen)
    
    def enlazar (self, tv):
        if self.tv:
            tv.setControl(self)
            self._tv = tv
    
    def getTv (self):
        return self._tv
    
    def setTv (self , tv):
        self._tv=tv
