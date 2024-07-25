print('Hello World') 
print('Pas de virgule , ni point virgule , sauf sur la meme ligne') 
# Les variables
# a=5 ; b=12
# print (a+b)
# mon_nom = 'FREDERIC'
# print(type(mon_nom))
# nombre1 = 5
# print(type(nombre1))
# mon_bool = True
# print(type(mon_bool))
# mon_tableau = [1,2,3,4,5,6]
# print(type(mon_tableau))
# mon_dico={'Key1':'value','Key1':'value'}
# print(type(mon_dico))
# mon_tuple = (1,2,3,4,5,6)
# print(type(mon_tuple))
# mon_set = {1,2,3,4,5,6}
# print(type(mon_set))
# print('je m appelle : {mon_nom} et j ai {nombre1} ans ')
a,b,c=1,2,3
a=10;b=5
result = a+b
mon_message= f"{a}+{b}={result}"
print(mon_message)

# Conversion

# mon_entree = int(input('veuillez-entrez un nombre')) 
# print(type(mon_entree))

mon_entree = eval(input('veuillez-entrez un nombre')) 
print(type(mon_entree))
# entrée / sortie console
print('Salut','bonjour',mon_entree,sep='\t',end='!!!!!\n')


