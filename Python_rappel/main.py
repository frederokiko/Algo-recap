# x=5

# if x>5 : 
#     print("coucou")

# while x<10 :
#     print("x")
#     x+=1 

# def maMethode():
#     print("coucou")

# maMethode()
from models.voiture import Voiture

v1 = Voiture("rouge",4,1000)
v2 = Voiture("vert",6,2000)
print(v1.couleur,v1.cylindre,v1.Prix)
print(v2.couleur,v2.cylindre,v2.Prix)
v1.Prix=2400
v2.Prix=4002
print(v1.couleur,v1.Prix)
print(v2.couleur,v2.Prix)