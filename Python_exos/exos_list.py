#exos01

# Commencez par créer une liste de 10 nombres aléatoires compris entre 1 et 100. Ensuite, affichez cette liste générée.
# Après cela, calculez la somme de tous les éléments de la liste et affichez-la.

# import random
# total=0
# ma_list=[]
# for i in range(0,10,1):
#     nombre=random.randint(1,100)
#     ma_list.append(nombre)
# print(ma_list)
# for result in ma_list:
#     total+=result
# print(total)

#exos02

#  Invitez l'utilisateur à saisir son prénom et son nom. Ensuite, créez un tuple contenant ces informations. Pour finir,
# affichez séparément le prénom et le nom à partir du tuple.

# nom =input('votre nom :')
# prenom = input('votre prenom :')
# mon_tuple=(nom,prenom)
# print(mon_tuple[0])
# print(mon_tuple[1])

#exos03

# Générez deux ensembles de nombres aléatoires compris entre 1 et 20. Affichez ces deux ensembles générés. Enfin,
# trouvez l'intersection des deux ensembles et affichez-la

# tab1=set([])
# tab2=set([])

# for i in range(1,21,1):
#     tab1.add(i)
#     tab2.add(i)
#     i+=1
# print(tab1)
# print(tab2)
# tab3=tab1.intersection(tab2)
# print(tab3)

# exos04

# Créez un dictionnaire contenant les prix de quelques fruits tels que la pomme, la banane et l'orange. Demandez à
# l'utilisateur de saisir le nom d'un fruit, puis affichez le prix correspondant à ce fruit s'il existe dans le dictionnaire.

# dictionnaire={"pomme":2.45,"banane":2.1,"orange":3.5}
# choix=input('Choisissez un fruit pomme : banane : orange')
# if choix in dictionnaire :
#     print(f'Le prix de l article {choix} est de {dictionnaire.get(choix)} €')
# else :
#     print('choix incorrect')
#exos05

# Créez une liste de tuples contenant le nom et l'âge de trois personnes. Trouvez ensuite la personne la plus âgée et
# affichez son nom.

# plus_age=0
# nom=['robert','jean','pierre','pol']
# age=[45,65,35,54]
# mon_tuple = (nom,age)
# for nbr in mon_tuple[1]:
#     if nbr>plus_age:
#         plus_age=nbr
# index=mon_tuple[1].index(plus_age)
# print(f'le plus age est : {mon_tuple[0][index]}')

#exos06

#  Générez une liste de 10 nombres aléatoires compris entre 1 et 50. Affichez cette liste générée. Ensuite, filtrez les
# nombres pairs de la liste et créez une nouvelle liste ne contenant que ces nombres pairs. Enfin, affichez la nouvelle
# liste contenant uniquement les nombres pairs.

# import random
# ma_list=[]
# nbr_pair =[]
# for i in range(0,10,1):
#     nombre=random.randint(1,50)
#     ma_list.append(nombre)
# print(ma_list)
# for nbr in ma_list:
#     if nbr%2==0:
#         nbr_pair.append(nbr)
# print(nbr_pair)

# exos07

# Créez une liste de mots contenant des doublons. Transformez ensuite cette liste en un ensemble pour éliminer les
# doublons. Affichez l'ensemble résultant.

# list_double=['pipi','toto','jean','coco','fifi','toto','pipi','coco','pipi']
# sans_doublon=[]
# for text in list_double:
#     result=sans_doublon.count(text)
#     if result==0:
#         sans_doublon.append(text)
# print(sans_doublon)

# exos08

# Créez un dictionnaire de listes représentant différents cours et les étudiants inscrits dans chaque cours. Ajoutez des
# étudiants à chaque cours. Ensuite, demandez à l'utilisateur de saisir le nom d'un cours et affichez la liste des
# étudiants inscrits à ce cours.

# list_cours=['mathematique','français','biochimie','anglais']
# list_student=['fred','mika','nathan','antho','lili','jojo','quentin']

# import random
# ma_list=[random.randint(0,100) for _ in range(10)]
# print (ma_list)