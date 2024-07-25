class Vehicule :
   def __init__(self,c,p) :
        self.couleur = c
        self.roue = 4
        self.__prix = p

@property
def Prix(self):# getter
        return self.__prix * 1.21
    
@Prix.setter
def Prix(self,value):#setter
    self.__prix = value