class Voiture:
    def __init__(self,c,cyl,p) :
        self.couleur = c
        self.roue = 4
        self.cylindre =cyl # rend le membre private
        self.__prix = p

    # def _get_Prix(self):# getter
    #     return self.__prix * 1.21
    
    # def _set_Prix(self,value):#setter
    #     self.__prix = value

    @property
    def Prix(self):# getter
        return self.__prix * 1.21
    
    @Prix.setter
    def Prix(self,value):#setter
        self.__prix = value