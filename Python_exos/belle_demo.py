#region creation de liste
ma_liste=[]
ma_liste.append('Bonjour') #ajoute à la fin
#print(ma_liste)
print('-------------------------')
#constructeur
ma_liste = list("hello world")
#print(ma_liste)

#endregion
print('-------------------------')
#region ajout d'ellement

ma_liste=["Hello","Toto"]
ma_liste.append('Bonjour')
#print(ma_liste)
for el in ma_liste :
    print(el)
print('-------------------------')
ma_liste.insert(1,"coucou")
for el in ma_liste :
    print(el)
print('-------------------------')
ma_liste.extend([1,2,3,4])#ou variable tableau
for el in ma_liste :
    print(el)
print('-------------------------')
compte =len(ma_liste)
print(compte)
#endregion
#region suppression
ma_liste.remove("coucou")
for el in ma_liste :
    print(el)
print('-------------------------')
result= ma_liste.pop(1)
print(result)

list_temp = ma_liste
#ma_liste.clear()
print('-------------------------')
for el in ma_liste :
    print(el)
print('la liste à eté vidée de tout')
print('-------------------------')
#endregion
#region recherche
ma_liste=list_temp
for el in ma_liste :
    print(el)
index=ma_liste.index('Hello')
print(index)
ma_liste.append('Toto')
ma_liste.append('Toto')
ma_liste.append('Toto')
ma_liste.append('Toto')
result=ma_liste.count('Toto')
print(result)
print('-------------------------')
ma_liste=[9,8,7,6,5,4,3,2,1,0]
for el in ma_liste :
    print(el)
ma_liste.sort()
for el in ma_liste :
    print(el)
ma_liste.reverse()
for el in ma_liste :
    print(el)
list_copy = ma_liste.copy()
print(list_copy)




#endregion

#import random
# ma_list=[random.randint(0,100) for _ in range(10)]
# print (ma_list)
